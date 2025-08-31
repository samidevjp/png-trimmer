# 1. プロジェクトフォルダ作成

mkdir png-trimmer && cd png-trimmer

# 2. 必要なフォルダ作成

mkdir images output_folder

# 3. main.py を作成

cat << 'EOF' > main.py
import os
from PIL import Image

def trim_transparency(image_path, output_path): # PNG 画像の読み込み
img = Image.open(image_path)

    # 画像がRGBAでない場合、変換する
    if img.mode != 'RGBA':
        img = img.convert('RGBA')

    # 画像データを取得
    datas = img.getdata()

    # 透明な部分を示すフラグ
    non_empty_pixels = []
    for y in range(img.height):
        for x in range(img.width):
            if datas[y * img.width + x][3] != 0:
                non_empty_pixels.append((x, y))

    # 透明部分がない場合
    if not non_empty_pixels:
        print("The image {} has no non-transparent pixels.".format(image_path))
        return

    # 透明でない部分の最小の矩形領域を計算
    min_x = min(non_empty_pixels, key=lambda t: t[0])[0]
    max_x = max(non_empty_pixels, key=lambda t: t[0])[0]
    min_y = min(non_empty_pixels, key=lambda t: t[1])[1]
    max_y = max(non_empty_pixels, key=lambda t: t[1])[1]

    # 画像をトリミング
    cropped_img = img.crop((min_x, min_y, max_x + 1, max_y + 1))

    # 新しい画像を保存
    cropped_img.save(output_path)

# フォルダ内のすべての PNG ファイルに適応

folder_path = "./images"
output_folder_path = "./output_folder"

# 出力フォルダが存在しない場合、作成する

if not os.path.exists(output_folder_path):
os.makedirs(output_folder_path)

# フォルダ内の PNG ファイルをループ

for file_name in os.listdir(folder_path):
if file_name.endswith(".png"):
input_path = os.path.join(folder_path, file_name)
output_path = os.path.join(output_folder_path, file_name)
trim_transparency(input_path, output_path)

print("Trimming completed!")
EOF

# 4. requirements.txt を作成

cat << 'EOF' > requirements.txt
Pillow
EOF

# 5. README.md を作成

cat << 'EOF' > README.md

# PNG Transparency Trimmer

This project trims transparent edges from PNG images automatically.

---

## Requirements

- Python 3.8 or later
- pip (Python package manager)

---

## Installation

1. **Clone the repository or download the files**
   \`\`\`bash
   git clone https://github.com/your-username/png-trimmer.git
   cd png-trimmer
   \`\`\`

2. **Install dependencies**
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

---

## Usage

1. **Prepare your images**

   - Place PNG files you want to trim inside the \`images/\` folder.
   - Example:
     \`\`\`
     images/
     ├── sample1.png
     ├── sample2.png
     \`\`\`

2. **Run the script**
   \`\`\`bash
   python main.py
   \`\`\`

3. **Check the results**
   - The trimmed PNG files will be saved in the \`output_folder/\`.
   - Example:
     \`\`\`
     output_folder/
     ├── sample1.png # trimmed version
     ├── sample2.png # trimmed version
     \`\`\`

---

## Notes

- Only \`.png\` files are processed.
- If an image has no transparent area, the script will skip trimming.
- You can modify \`folder_path\` and \`output_folder_path\` in \`main.py\` to change input/output directories.
  EOF

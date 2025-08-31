import os
from PIL import Image

def trim_transparency(image_path, output_path):
    # PNG画像の読み込み
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

# フォルダ内のすべてのPNGファイルに適応
folder_path = "./images"
output_folder_path = "./output_folder"

# 出力フォルダが存在しない場合、作成する
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# フォルダ内のPNGファイルをループ
for file_name in os.listdir(folder_path):
    if file_name.endswith(".png"):
        input_path = os.path.join(folder_path, file_name)
        output_path = os.path.join(output_folder_path, file_name)
        trim_transparency(input_path, output_path)

print("Trimming completed!")


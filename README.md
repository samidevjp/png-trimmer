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

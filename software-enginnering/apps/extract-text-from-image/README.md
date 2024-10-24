## Python OCR Text Extraction

### Description

This Python script uses **Pillow** and **Tesseract OCR** to extract text from images and save it into `.txt` files. After extraction, the text file is opened automatically.

### Installation

Steps to set up the project locally:

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Install Tesseract OCR and configure the path:
   - [Download Tesseract](https://sourceforge.net/projects/tesseract-ocr-alt/files/)
   - Update the script with your Tesseract path:

     ```python
     pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
     ```

### Usage

1. Modify the `image_paths` list with the image names:

   ```python
   image_paths = ["1.jpeg", "2.png"]
   ```

2. Run the script:

   ```bash
   python your_script.py
   ```

3. Text will be extracted and saved as `.txt` files in the same directory.

### Main Functions

- `extract_text_from_image(image_path)`: Extracts text from an image.
- `save_text_to_file(text, image_path)`: Saves and opens the extracted text file.

### Requirements

Command instalation `pip install -r requirements.txt`

- Python
- Pillow
- Tesseract OCR
- `opencv-python`
- VS Code extensions: `Pylance`, `Python Debugger`, `PyLint`, `Ruff`

### Notes

- Tesseract must be properly installed, and the script is set up for Windows. Adjustments may be needed for other systems.

### Author

Maintained by [Sabrina B.](https://github.com/sabrinabm94/about/blob/main/README.md).
Feel free to reach out at <sabrinabm94@gmail.com>.

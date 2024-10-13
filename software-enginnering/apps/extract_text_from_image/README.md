# README

## Description

This Python script uses the **PIL** (Pillow) library and **Tesseract OCR** to extract text from images and save it into text files (.txt). After extraction, the generated text file is opened automatically.

## Dependencies

### 1. Python

Make sure you have Python installed. You can install the necessary dependencies using the `pip` package manager. Run the following commands in your terminal or command prompt:

```bash
pip install pillow
pip install pytesseract
pip install opencv-python
```

### 2. Required Software

To ensure the project works properly, you will need **Tesseract OCR**. Follow the steps below:

1. **Download and Install Tesseract**:
   - Go to the Tesseract download page: [Download Tesseract](https://sourceforge.net/projects/tesseract-ocr-alt/files/).

2. **Configure the Tesseract Path**:
   - After installation, locate the path where Tesseract was installed.
   - Update the script to include the path to the Tesseract executable, as exemplified below:

     ```python
     pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
     ```

## How to Use

1. **Prepare Images**:
   - Make sure the images from which you want to extract text are in the same directory as the script, or provide the full path.

2. **Modify the Script**:
   - Edit the `image_paths` list to include the names of the images you want to process. For example:

     ```python
     image_paths = [
         "1.jpeg",
         "2.png",
     ]
     ```

3. **Run the Script**:
   - Execute the script in your Python environment:

     ```bash
     python your_script.py
     ```

4. **Results**:
   - The extracted text will be saved in `.txt` files in the same directory as the images. After extraction, each text file will be opened automatically.

## Main Functions

- `extract_text_from_image(image_path)`: Extracts text from a specified image.
- `save_text_to_file(text, image_path)`: Saves the extracted text in a `.txt` file and opens it automatically.

## Notes

- Ensure that Tesseract is installed correctly and that the path is configured in the script.
- The script is optimized to run in Windows environments. For other operating systems, you may need to modify the line that opens the text file.

## Author

Sabrina B.
See my profile [here](https://github.com/sabrinabm94/about/blob/main/README.md)
<sabrinabm94@gmail.com>

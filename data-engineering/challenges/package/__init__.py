import pytesseract
import os

import extract_text_from_image
import processing_image
import generate_file

# Indique o local de instalação do Tesseract na sua máquina
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
)

# Obtém o diretório onde o script está localizado
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construa o caminho completo da imagem
image_paths = [
    os.path.join(script_dir, "image.png"),
]


# Extraindo texto das imagens e salvando em arquivos .txt
for image_path in image_paths:
    image = processing_image.process_image(image_path)

    if image:
        extracted_text = extract_text_from_image.extract_text_from_image(image_path)

        if extracted_text:
            generate_file.save_text_to_file(extracted_text, image_path)

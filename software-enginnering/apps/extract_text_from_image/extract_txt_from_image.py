from PIL import Image
import pytesseract
import os

# Indique o local de instalação do Tesseract na sua máquina
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
)

# Indique o diretório e nome da imagem que deseja extrair o texto
image_paths = [
    "1.jpeg",
]


# Função para extrair texto de uma imagem
def extract_text_from_image(image_path):
    if os.path.exists(image_path):
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text
    else:
        return f"Arquivo não encontrado: {image_path}"


# Salvando texto extraído em arquivos .txt
def save_text_to_file(text, image_path):
    # Gerar o nome do arquivo .txt baseado no nome da imagem
    txt_file_name = os.path.splitext(image_path)[0] + ".txt"
    with open(txt_file_name, "w", encoding="utf-8") as file:
        file.write(text)
    print(f"Texto extraído salvo em: {txt_file_name}")

    # Abrir o arquivo .txt automaticamente
    os.startfile(txt_file_name)  # Para Windows
    # subprocess.Popen(['notepad.exe', txt_file_name])  # Alternativa se não funcionar


# Extraindo texto das imagens e salvando em arquivos .txt
for image_path in image_paths:
    extracted_text = extract_text_from_image(image_path)
    save_text_to_file(extracted_text, image_path)

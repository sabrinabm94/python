from PIL import Image
import pytesseract


# Função para extrair texto de uma imagem
def extract_text_from_image(image):
    if image:
        text = pytesseract.image_to_string(image)
        return text
    else:
        print(f"Não foi possível extrair o texto da imagem!")
        return None

from PIL import Image
import os


# Função para processar imagem de um diretório
def process_image(image_path):
    if os.path.exists(image_path):
        image = Image.open(image_path)
        if image:
            print("Imagem processada com sucesso!")
            return image
        else:
            print(f"Arquivo não encontrado: {image_path}")
            return None

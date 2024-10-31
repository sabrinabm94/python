import os
import extract_text_from_image
import processing_image
import generate_file


def main(image_name, image_path):
    image_paths = [
        os.path.join(image_path, image_name),
    ]

    # Extraindo texto das imagens e salvando em arquivos .txt
    for image_path in image_paths:
        image = processing_image.process_image(image_path)

        if image:
            extracted_text = extract_text_from_image.extract_text_from_image(image_path)

            if extracted_text:
                generate_file.save_text_to_file(extracted_text, image_path)


# Preencher com as info da sua imagem
image_name = "image.png"
image_path = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    main(image_name, image_path)

# Data Engineering Challenges Package

Este pacote Python utiliza Pillow e Tesseract OCR para extrair texto de imagens e salvar o conteúdo em arquivos .txt. Após a extração, o arquivo de texto é aberto automaticamente para visualização.

## Instalação

Adicione o pacote utilizando o comando abaixo

```bash
pip install read-text-from-image-with-python
```

Disponibilizado via [pypi](https://pypi.org/project/read-text-from-image-with-python/).

## Uso

### Módulos Disponíveis

Cada módulo oferece funcionalidades específicas para processamento de imagem e texto:

1. **extract_text_from_image**
   **Função `extract_text_from_image(image)`**: Extrai o texto de uma imagem fornecida. Retorna o texto extraído ou None se não for possível realizar a extração.

2. **generate_file**
   **Função `save_text_to_file(text, image_path`**: Salva o texto extraído em um arquivo .txt, cujo nome é baseado no nome da imagem original, e abre o arquivo automaticamente para visualização.

3. **processing_image**
   **Função `process_image(image_path)`**: Processa uma imagem a partir de um diretório e a prepara para a extração de texto. Retorna o objeto da imagem se for processado com sucesso, ou None se o arquivo de imagem não for encontrado.

### Exemplo de uso

```python
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

```

---

### Notes

- O Tesseract precisa estar instalado corretamente, e este script foi configurado para sistemas Windows. Para outros sistemas, ajustes podem ser necessários.

### Author

Mantido por [Sabrina B. Moreira](https://github.com/sabrinabm94/about/blob/main/README.md).
Entre em contato em <sabrinabm94@gmail.com>.

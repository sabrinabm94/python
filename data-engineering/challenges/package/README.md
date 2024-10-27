## Python OCR Text Extraction Package

### Description

Este pacote Python utiliza **Pillow** e **Tesseract OCR** para extrair texto de imagens e salvar o conteúdo em arquivos `.txt`. Após a extração, o arquivo de texto é aberto automaticamente para visualização.

### Installation

Pode ser instalado o pacote publicado em: <https://pypi.org/project/read-text-from-image-with-python/>
ou seguindo os passos baixo para rodar o compilado:
Passos para configurar o projeto localmente:

1. Clone o repositório.
2. Instale as dependências com o comando:

   ```bash
   pip install -r requirements.txt
   ```

3. Instale o Tesseract OCR e configure o caminho:
   - [Baixar Tesseract](https://sourceforge.net/projects/tesseract-ocr-alt/files/)
   - Atualize o caminho para o Tesseract no script:

     ```python
     pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
     ```

### Package Modules

O pacote está dividido em três módulos principais:

1. **extract_text_from_image** (`data-engineering/challenges/package/extract_text_from_image/__init__.py`):
   - Função `extract_text_from_image(image)`: Extrai o texto de uma imagem fornecida. Retorna o texto extraído ou `None` se não for possível realizar a extração.

2. **generate_file** (`data-engineering/challenges/package/generate_file/__init__.py`):
   - Função `save_text_to_file(text, image_path)`: Salva o texto extraído em um arquivo `.txt`, cujo nome é baseado no nome da imagem original, e abre o arquivo automaticamente para visualização.

3. **processing_image** (`data-engineering/challenges/package/processing_image/__init__.py`):
   - Função `process_image(image_path)`: Processa uma imagem a partir de um diretório e a prepara para a extração de texto. Retorna o objeto da imagem se for processado com sucesso, ou `None` se o arquivo de imagem não for encontrado.

### Usage

1. Substitua `image_paths` pela lista de imagens desejada:

   ```python
   image_paths = ["1.jpeg", "2.png"]
   ```

2. Execute o script principal para extrair e salvar o texto:

   ```bash
   python your_script.py
   ```

3. O texto extraído será salvo como arquivos `.txt` no mesmo diretório da imagem.

### Requirements

Instale os requisitos com o comando:

```bash
pip install -r requirements.txt
```

- Python
- Pillow
- Tesseract OCR
- `opencv-python` (se necessário para manipulação de imagens)

### Notes

- O Tesseract precisa estar instalado corretamente, e este script foi configurado para sistemas Windows. Para outros sistemas, ajustes podem ser necessários.

### Author

Mantido por [Sabrina B. Moreira](https://github.com/sabrinabm94/about/blob/main/README.md).
Entre em contato em <sabrinabm94@gmail.com>.

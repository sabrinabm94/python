import cv2
import pytesseract

# Carregando a imagem do documento
# imagem_documento_path = "./image.jpeg"
imagem_documento_path = "./hello.png"
imagem_documento = cv2.imread(imagem_documento_path)

if imagem_documento:
    # Convertendo a imagem para escala de cinza
    imagem_documento_cinza = cv2.cvtColor(imagem_documento, cv2.COLOR_BGR2GRAY)

    # Aplicando binarização (thresholding)
    _, imagem_documento_binaria = cv2.threshold(
        imagem_documento_cinza, 128, 255, cv2.THRESH_BINARY
    )

    # Aplicando OCR na imagem do documento
    texto_documento = pytesseract.image_to_string(imagem_documento_binaria, lang="por")

    print(f"Texto no Documento: {texto_documento}")

else:
    print("Imagem não encontrada!")

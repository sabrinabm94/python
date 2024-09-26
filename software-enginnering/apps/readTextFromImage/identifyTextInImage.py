import cv2
import pytesseract

# Substitua pelo caminho correto no seu sistema
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # TODO: trocar para o caminho da sua instalação

# Detecção de contornos na imagem
contornos, _ = cv2.findContours(
    imagem_sem_ruido, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)

# Iterando sobre os contornos encontrados
for contorno in contornos:
    # Ignorando contornos muito pequenos
    if cv2.contourArea(contorno) > 100:
        # Obtendo as coordenadas do retângulo que envolve o contorno
        x, y, w, h = cv2.boundingRect(contorno)

        # Desenhando o retângulo na imagem original
        cv2.rectangle(imagem, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Recortando a região de texto da imagem original
        regiao_texto = imagem[y : y + h, x : x + w]

        # Aplicando OCR na região de texto
        texto_detectado = pytesseract.image_to_string(
            regiao_texto, lang="por"
        )  # Use o idioma adequado

        # Imprimindo o texto detectado
        print(f"Texto Detectado: {texto_detectado}")

# Exibindo a imagem com os contornos e retângulos
cv2.imshow("Imagem com Contornos", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()

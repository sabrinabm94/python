import cv2

# Carregando a imagem
imagem_path = "./image.jpeg"  # TODO: Substitua pelo caminho da sua imagem
imagem = cv2.imread(imagem_path)

# Verificando se a imagem foi carregada corretamente
if imagem is None:
    print("\nErro ao carregar a imagem.\n")
else:
    print("\nImagem carregada com sucesso.\n")

    # Convertendo a imagem para escala de cinza
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # Aplicando binarização (thresholding)
    _, imagem_binaria = cv2.threshold(imagem_cinza, 128, 255, cv2.THRESH_BINARY)

    # Aplicando um filtro para remover ruídos (opcional)
    imagem_sem_ruido = cv2.medianBlur(imagem_binaria, 5)

    # Ajustando o contraste (opcional)
    alpha = 1.5  # Fator de contraste
    beta = 50  # Fator de brilho
    imagem_processada = cv2.convertScaleAbs(imagem_sem_ruido, alpha=alpha, beta=beta)

    # Exibindo a imagem original e a imagem processada
    cv2.imshow("Imagem Original", imagem)
    cv2.imshow("Imagem Processada", imagem_processada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

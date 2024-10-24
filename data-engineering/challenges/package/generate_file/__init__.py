import os


# Salva um texto em um arquivo .txt e abre o arquivo automaticamente
def save_text_to_file(text, image_path):
    # Gerar o nome do arquivo .txt baseado no nome da imagem
    txt_file_name = os.path.splitext(image_path)[0] + ".txt"
    with open(txt_file_name, "w", encoding="utf-8") as file:
        file.write(text)
    print(f"Texto extraído salvo em: {txt_file_name}")

    # Abrir o arquivo .txt automaticamente
    os.startfile(txt_file_name)  # Para Windows
    # subprocess.Popen(['notepad.exe', txt_file_name])  # Alternativa se não funcionar

# For
# Usado para percorrer um objeto iterável ou quando sabemos exatamente a quantidade de vezes que desejamos repetir uma instrução

# Exemplo 1
for number in range(10):
    if number == 8:  # o range será de 0-7, encerra a execução em 7
        break
    if number == 2:  # 2 não será executado, pula a execução do 2
        continue

    print(number)

# Exemplo 2
text = str(input("Digite uma palavra e veja cada uma de suas letras: "))
for letter in text:
    print(letter)

# input: armazenamento de informações vindas do terminal do usuário
name = input("Digite o seu nome: ")
age = input("Digite a sua idade: ")

# output: envio de informações para o usuário
print(name, age)
print(name, end="...\n")
print(age, end="\n")
print(name, age, sep="#")

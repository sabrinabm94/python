# White
# Repete um bloco de código várias vezes onde não sabemos até quando deverá ser executado, não tem número fixo.

option = -1

while option != 0:
    option = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n:"))
    if option == 1:
        print("Sacando...")
    elif option == 2:
        print("Exibindo extrato...")

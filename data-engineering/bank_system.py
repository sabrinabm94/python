balance_value = 3300
option = -1

while option != 4:
    option = int(input("[1] Sacar \n[2] Extrato \n[3] Cancelar \n[4] Sair \n:"))
    if option == 1:
        print(f"Você tem {balance_value} na sua conta")
        withdrawal_value = float(input("Informe o valor de saque:"))
        balance_value -= withdrawal_value
        print(f"Valor de {withdrawal_value} sacado com sucesso!")
    if option == 2:
        print("Exibindo extrato...")
        print("Seu valor total na conta é:", balance_value)
    if option == 3:
        print("Cancelando...")
        break

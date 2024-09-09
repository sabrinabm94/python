import sys

balance_value = 3300
option = int(input("Informe a sua opção: [1] Sacar valor \n [2]Extrato de conta \n"))

if option == 1:
    withdrawal_value = float(input("Informe o valor de saque:"))
    balance_value -= withdrawal_value
    print(f"Valor de {withdrawal_value} sacado com sucesso!")
elif option == 2:
    print("Seu valor total na conta é:", balance_value)
else:
    sys.exit("Opção inválida, saindo do sistema...")

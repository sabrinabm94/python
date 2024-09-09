balance = float(1000)
withdrawal = float(input("Informe o valor da retirada: "))

if balance >= withdrawal:
    balance -= withdrawal
    print(f"Saque de {withdrawal} realizado com sucesso!, seu saldo atual é {balance}")
elif balance < withdrawal:
    print(f"Valor de saque {withdrawal} não permitido, tente novamente.")
else:
    print("Não foi possível realizar a operação, tente novamente.")

balance_value = 300
withdrawal_per_day_limit = 3
withdrawal_in_day_number = 0
deposite_in_day_number = 0
withdrawal_per_operation_value_limit = 500.00
option = -1


def show_menu():
    return """Seja bem vindo!
    Selecione uma opção para continuar:
            [1] Depósito
            [2] Saque
            [3] Extrato
            [4] Cancelar
            [4] Sair
    Obrigado por usar nosso sistema.
    """


def deposite_value(balance_value, deposite_in_day_number):
    print("\nOpção DEPÓSITO selecionada...")
    show_balance_value(balance_value)
    deposite_value = float(input("Informe o valor de depósito:"))
    if deposite_value > 0:
        balance_value += deposite_value
        deposite_in_day_number += 1
        print(f"Valor de R$ {deposite_value} depositado com sucesso!")
        print("Depósitos realizados no dia:", deposite_in_day_number)
    else:
        print("Valor de depósito inválido!")
    return balance_value, deposite_in_day_number


def withdrawal_value(
    balance_value,
    withdrawal_per_day_limit,
    withdrawal_in_day_number,
    withdrawal_per_operation_value_limit,
):
    print("\nOpção SAQUE selecionada...")
    show_balance_value(balance_value)
    if withdrawal_in_day_number < withdrawal_per_day_limit:
        withdrawal_value = float(input("Informe o valor de saque:"))
        if (
            withdrawal_value > 0
            and withdrawal_value <= withdrawal_per_operation_value_limit
        ):
            if withdrawal_value <= balance_value:
                balance_value -= withdrawal_value
                withdrawal_in_day_number += 1
                print(f"Valor de {withdrawal_value} sacado com sucesso!")
                print(
                    f"Saques realizados no dia: {withdrawal_in_day_number}/{withdrawal_per_day_limit}"
                )
            else:
                print(
                    "Saque não realizado! O valor de saque é superior ao seu saldo em conta."
                )
        else:
            print("Valor de saque inválido!")
    else:
        print("limite de saque para a operação já alcançado!")

    return balance_value, withdrawal_in_day_number


def balance_show(balance_value):
    print("\nOpção EXTRATO selecionada...")
    show_balance_value(balance_value)
    show_withdrawal_in_day_number(withdrawal_in_day_number, withdrawal_per_day_limit)
    show_deposite_in_day_number(deposite_in_day_number)


def show_balance_value(balance_value):
    print("Seu valor total na conta é: R$", balance_value)


def show_withdrawal_in_day_number(withdrawal_in_day_number, withdrawal_per_day_limit):
    print(
        f"Saques realizados no dia: {withdrawal_in_day_number}/{withdrawal_per_day_limit} "
    )


def show_deposite_in_day_number(deposite_in_day_number):
    print("Depósitos realizados no dia:", deposite_in_day_number)


while option != 5:
    option = int(input(show_menu()))

    if option == 1:
        balance_value, deposite_in_day_number = deposite_value(
            balance_value, deposite_in_day_number
        )
    if option == 2:
        balance_value, withdrawal_in_day_number = withdrawal_value(
            balance_value,
            withdrawal_per_day_limit,
            withdrawal_in_day_number,
            withdrawal_per_operation_value_limit,
        )
    if option == 3:
        balance_show(balance_value)
    if option == 4:
        print("Opção CANCELAR selecionada, cancelando...")
        break

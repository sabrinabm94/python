from datetime import datetime

balance_value = 300
withdrawal_transaction_per_day_limit_number = 3
transactions_per_day_limit = 10
transactions_in_day_number = 0
withdrawal_transaction_in_day_number = 0
deposite_in_day_number = 0
withdrawal_per_operation_limit_value = 500.00
option = -1
transactions_history = ""


def deposite_transaction_value(
    balance_value,
    deposite_in_day_number,
    transactions_in_day_number,
    transactions_per_day_limit,
    transactions_history,
):
    print("\nOpção DEPÓSITO selecionada...")
    show_balance_value(balance_value)
    transaction_date_time = datetime.now()
    is_transaction_allowed = transactions_in_day_limit_verify(
        transaction_date_time, transactions_per_day_limit, transactions_in_day_number
    )
    if is_transaction_allowed is True:
        deposite_transaction_value = float(input("Informe o valor de depósito:"))
        if deposite_transaction_value > 0:
            balance_value += deposite_transaction_value
            deposite_in_day_number += 1
            transactions_in_day_number += 1
            transactions_history = update_transactions_history(
                transactions_history,
                transaction_date_time,
                deposite_transaction_value,
                "depositado",
            )
            show_transaction_confirmation_message(
                deposite_transaction_value, "depositado"
            )
            print("Depósitos realizados no dia:", deposite_in_day_number)
            show_transactions_in_day_number(
                transactions_in_day_number, transactions_per_day_limit
            )
            show_balance_value(balance_value)

        else:
            print("Valor de depósito inválido!")

    return (
        balance_value,
        deposite_in_day_number,
        transactions_in_day_number,
        transactions_history,
    )


def withdrawal_transaction_value(
    balance_value,
    withdrawal_transaction_per_day_limit_number,
    withdrawal_transaction_in_day_number,
    withdrawal_per_operation_limit_value,
    transactions_in_day_number,
    transactions_history,
):
    print("\nOpção SAQUE selecionada...")
    show_balance_value(balance_value)
    transaction_date_time = datetime.now()
    is_transaction_allowed = transactions_in_day_limit_verify(
        transaction_date_time, transactions_per_day_limit, transactions_in_day_number
    )
    is_withdrawal_transaction_allowed = withdrawal_transactios_in_day_limit_verify(
        transaction_date_time,
        withdrawal_transaction_per_day_limit_number,
        withdrawal_transaction_in_day_number,
    )
    if is_transaction_allowed is True:
        if is_withdrawal_transaction_allowed is True:
            withdrawal_transaction_value = float(input("Informe o valor de saque:"))
            is_withdrawal_transaction_value_valid = withdrawal_value_verify(
                transaction_date_time,
                withdrawal_transaction_value,
                withdrawal_per_operation_limit_value,
                balance_value,
            )
            if is_withdrawal_transaction_value_valid is True:
                balance_value -= withdrawal_transaction_value
                withdrawal_transaction_in_day_number += 1
                transactions_in_day_number += 1
                transactions_history = update_transactions_history(
                    transactions_history,
                    transaction_date_time,
                    withdrawal_transaction_value,
                    "sacado",
                )
                show_transaction_confirmation_message(
                    withdrawal_transaction_value, "sacado"
                )
                show_withdrawal_transactions_in_day_number(
                    withdrawal_transaction_in_day_number,
                    withdrawal_transaction_per_day_limit_number,
                )
                show_transactions_in_day_number(
                    transactions_in_day_number, transactions_per_day_limit
                )
                show_balance_value(balance_value)
            else:
                print(f"Valor de saque de {withdrawal_transaction_value} é inválido!")
        else:
            print(
                f"O limite de {withdrawal_transaction_per_day_limit_number} saques diários foi batido, tente novamente amanhã! "
            )

    return (
        balance_value,
        withdrawal_transaction_in_day_number,
        transactions_in_day_number,
        transactions_history,
    )


def show_balance(
    balance_value,
    withdrawal_transaction_in_day_number,
    withdrawal_transaction_per_day_limit_number,
    deposite_in_day_number,
    transactions_in_day_number,
    transactions_history,
):
    print("\n\nOpção EXTRATO selecionada...")
    print("########### Extrato de conta ###########")
    show_balance_value(balance_value)

    # Somente mostra a quantidade de transações, depósitos e saques se tiverem sido realizadas operações no dia
    show_transactions_in_day_number(
        transactions_in_day_number, transactions_per_day_limit
    )
    if transactions_in_day_number > 0:
        show_withdrawal_transactions_in_day_number(
            withdrawal_transaction_in_day_number,
            withdrawal_transaction_per_day_limit_number,
        )
        show_deposite_transactions_in_day_number(deposite_in_day_number)
        print(f"\n Histórico de transações: {transactions_history} \n")

    print("########################################\n\n")


def show_menu():
    return """\n\nSeja bem vindo!
    Selecione uma opção para continuar:
            [1] Depósito
            [2] Saque
            [3] Extrato
            [4] Cancelar
    \n\n
    """


def show_balance_value(balance_value):
    print("Seu valor total na conta é: R$", balance_value)


def show_withdrawal_transactions_in_day_number(
    withdrawal_transaction_in_day_number, withdrawal_transaction_per_day_limit_number
):
    if withdrawal_transaction_in_day_number > 0:
        print(
            f"Saques realizados no dia: {withdrawal_transaction_in_day_number}/{withdrawal_transaction_per_day_limit_number} "
        )
    else:
        print("Não foram realizados saques no dia de hoje")


def show_deposite_transactions_in_day_number(deposite_in_day_number):
    if deposite_in_day_number > 0:
        print("Depósitos realizados no dia:", deposite_in_day_number)
    else:
        print("Não foram realizados depósitos no dia de hoje")

    return deposite_in_day_number


def show_transactions_in_day_number(
    transactions_in_day_number, transactions_per_day_limit
):
    if transactions_in_day_number > 0:
        if transactions_in_day_number <= transactions_per_day_limit:
            print(
                f"Transações realizadas no dia: {transactions_in_day_number}/{transactions_per_day_limit}"
            )
        else:
            print(
                f"O limite de {transactions_per_day_limit} transações diárias foi batido, tente novamente amanhã! "
            )
    else:
        print("Não foram realizadas transações no dia de hoje")

    return transactions_in_day_number


def get_date_now():
    date_time_now = datetime.now()
    if date_time_now:
        return date_time_now


def show_date_now(date_time_now):
    if date_time_now:
        print(f"Data: {date_time_now.date()} | Hora: {date_time_now.time()}")
        return date_time_now


def withdrawal_value_verify(
    transaction_date_time,
    withdrawal_transaction_value,
    withdrawal_per_operation_limit_value,
    balance_value,
):
    print(f"transaction_date_time {transaction_date_time}")
    print(f"withdrawal_transaction_value {withdrawal_transaction_value}")
    print(
        f"withdrawal_per_operation_limit_value {withdrawal_per_operation_limit_value}"
    )
    print(f"balance_value {balance_value}")

    if (
        withdrawal_transactios_in_day_limit_verify(
            transaction_date_time,
            withdrawal_transaction_per_day_limit_number,
            withdrawal_transaction_in_day_number,
        )
        is True
    ):
        if (
            withdrawal_transaction_value > 0
            and withdrawal_transaction_value <= balance_value
            and withdrawal_transaction_value <= withdrawal_per_operation_limit_value
        ):
            return True
        else:
            return False
    else:
        return False


def withdrawal_transactios_in_day_limit_verify(
    transaction_date_time,
    withdrawal_transaction_per_day_limit_number,
    withdrawal_transaction_in_day_number,
):
    today = get_date_now()

    print(f"\ntransaction_date_time {transaction_date_time}")
    print(f"today {today}")
    print(
        f"withdrawal_transaction_per_day_limit_number {withdrawal_transaction_per_day_limit_number}"
    )
    print(
        f"withdrawal_transaction_in_day_number {withdrawal_transaction_in_day_number}\n"
    )

    if transaction_date_time.date() <= today.date():
        if transaction_date_time.date() == today.date():
            # se as transações forem no mesmo dia, verifica o limite
            if (
                withdrawal_transaction_in_day_number
                < withdrawal_transaction_per_day_limit_number
            ):
                return True
            else:
                return False
    else:
        print("Não é possível realizar agendas de transações, cancelando operação...")
        return False


def transactions_in_day_limit_verify(
    transaction_date_time, transactions_per_day_limit, transactions_in_day_number
):
    today = get_date_now()

    # Se a data de transação for menor que hoje, é uma transação passada
    # Se a data de transação for igual a hoje, deve verificar o limite
    # Se a data de transação é maior que hoje, deve ser parado o código, não é permitido fazer agendamentos
    if transaction_date_time.date() <= today.date():
        if transaction_date_time.date() == today.date():
            # se as transações forem no mesmo dia, verifica o limite
            if transactions_in_day_number <= transactions_per_day_limit:
                return True
            else:
                return False
    else:
        print("Não é possível realizar agendas de transações, cancelando operação...")
        return False


def update_transactions_history(
    transactions_history,
    transaction_date_time,
    transaction_value,
    transaction_type_name,
):
    transactions_history += f"\nDia: {transaction_date_time.date()} | Hora: {transaction_date_time.time()} o valor de R$ {transaction_value} foi {transaction_type_name}."
    return transactions_history


def show_transaction_confirmation_message(transaction_value, transaction_type_name):
    return print(
        f"O valor de {transaction_value} foi {transaction_type_name} com sucesso!"
    )


while option != 5:
    option = int(input(show_menu()))

    if option == 1:
        (
            balance_value,
            deposite_in_day_number,
            transactions_in_day_number,
            transactions_history,
        ) = deposite_transaction_value(
            balance_value,
            deposite_in_day_number,
            transactions_in_day_number,
            transactions_per_day_limit,
            transactions_history,
        )
    if option == 2:
        (
            balance_value,
            withdrawal_transaction_in_day_number,
            transactions_in_day_number,
            transactions_history,
        ) = withdrawal_transaction_value(
            balance_value,
            withdrawal_transaction_per_day_limit_number,
            withdrawal_transaction_in_day_number,
            withdrawal_per_operation_limit_value,
            transactions_in_day_number,
            transactions_history,
        )
    if option == 3:
        show_balance(
            balance_value,
            withdrawal_transaction_in_day_number,
            withdrawal_transaction_per_day_limit_number,
            deposite_in_day_number,
            transactions_in_day_number,
            transactions_history,
        )
    if option == 4:
        print("Opção CANCELAR selecionada, cancelando...")
        print("Obrigada por usar o nosso sistema.\n")
        break

from datetime import datetime

balance_value = 300
withdrawal_transaction_per_day_limit_number = 3
transactions_per_day_limit = 10
transactions_in_day_number = 0
withdrawal_transaction_in_day_number = 0
deposit_in_day_number = 0
withdrawal_per_operation_limit_value = 500.00
option = -1
transactions_history = ""
account_agency = str("0001")
account_number_prefix = 0
accounts = []
users = [
    {
        "name": "Cassandra Souza",
        "birtdate": "15/05/1990",
        "cpf": "12345678900",
        "adress": "Rua das Flores, 123 - Centro - Florianópolis/SC",
    },
    {
        "name": "Nicolas Ferreira",
        "birtdate": "02/08/1985",
        "cpf": "98765432100",
        "adress": "Av. Paulista, 1000 - Bela Vista - São Paulo/SP",
    },
]


def deposit_transaction_value(
    balance_value,
    deposit_in_day_number,
    transactions_in_day_number,
    transactions_per_day_limit,
    transactions_history,
    user_cpf,
):
    print("\nOpção DEPÓSITO selecionada...")
    show_transaction_history_value(balance_value)
    transaction_date_time = datetime.now()
    is_transaction_allowed = transactions_in_day_limit_verify(
        transaction_date_time, transactions_per_day_limit, transactions_in_day_number
    )
    if is_transaction_allowed is True:
        deposit_transaction_value = float(input("Informe o valor de depósito:"))
        if deposit_transaction_value > 0:
            balance_value += deposit_transaction_value
            deposit_in_day_number += 1
            transactions_in_day_number += 1
            transactions_history = update_transactions_history(
                transactions_history,
                transaction_date_time,
                deposit_transaction_value,
                "depositado",
                user_cpf,  # Registrando CPF no histórico
            )
            show_transaction_confirmation_message(
                deposit_transaction_value, "depositado"
            )
            print("Depósitos realizados no dia:", deposit_in_day_number)
            show_transaction_history_value(balance_value)

        else:
            print("Valor de depósito inválido!")

    show_transactions_in_day_number(
        transactions_in_day_number, transactions_per_day_limit
    )
    return (
        balance_value,
        deposit_in_day_number,
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
    user_cpf,
):
    print("\nOpção SAQUE selecionada...")
    show_transaction_history_value(balance_value)
    transaction_date_time = datetime.now()
    is_transaction_allowed = transactions_in_day_limit_verify(
        transaction_date_time, transactions_per_day_limit, transactions_in_day_number
    )
    is_withdrawal_transaction_allowed = withdrawal_transactions_in_day_limit_verify(
        transaction_date_time,
        withdrawal_transaction_per_day_limit_number,
        withdrawal_transaction_in_day_number,
    )
    if is_transaction_allowed is True:
        if is_withdrawal_transaction_allowed is True:
            withdrawal_transaction_value = float(input("Informe o valor de saque:"))
            is_withdrawal_transaction_value_valid = withdrawal_value_verify(
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
                    user_cpf,  # Registrando CPF no histórico
                )
                show_transaction_confirmation_message(
                    withdrawal_transaction_value, "sacado"
                )
                show_withdrawal_transactions_in_day_number(
                    withdrawal_transaction_in_day_number,
                    withdrawal_transaction_per_day_limit_number,
                )
                show_transaction_history_value(balance_value)
            else:
                print(f"Valor de saque de {withdrawal_transaction_value} é inválido!")
        else:
            print(
                f"O limite de {withdrawal_transaction_per_day_limit_number} saques diários foi batido, tente novamente amanhã! "
            )

    show_transactions_in_day_number(
        transactions_in_day_number, transactions_per_day_limit
    )
    return (
        balance_value,
        withdrawal_transaction_in_day_number,
        transactions_in_day_number,
        transactions_history,
    )


def show_transaction_history(
    balance_value,
    withdrawal_transaction_in_day_number,
    withdrawal_transaction_per_day_limit_number,
    deposit_in_day_number,
    /,
    transactions_in_day_number,
    transactions_history,
    user_cpf,
):
    print("\n\nOpção EXTRATO selecionada...")
    print("\n########### Extrato de conta ###########\n")
    print(f"\n CPF: {user_cpf}")
    show_transaction_history_value(balance_value)

    # Somente mostra a quantidade de transações, depósitos e saques se tiverem sido realizadas operações no dia
    if transactions_in_day_number > 0:
        show_withdrawal_transactions_in_day_number(
            withdrawal_transaction_in_day_number,
            withdrawal_transaction_per_day_limit_number,
        )
        show_deposit_transactions_in_day_number(deposit_in_day_number)
        print(f"\nHistórico de transações: {transactions_history} \n")

    show_transactions_in_day_number(
        transactions_in_day_number, transactions_per_day_limit
    )
    print("########################################\n\n")


def update_transactions_history(
    transactions_history,
    transaction_date_time,
    transaction_value,
    transaction_type_name,
    user_cpf,
):
    transactions_history += f"\nDia: {transaction_date_time.date()} | Hora: {transaction_date_time.time()} | CPF: {user_cpf} | O valor de R$ {transaction_value} foi {transaction_type_name}."
    return transactions_history


def show_menu():
    return """\n\nSeja bem vindo!
    Selecione uma opção para continuar:
            [1] Cadastrar usuário
            [2] Listar usuários
            [3] Cadastrar conta bancária
            [4] Listar contas bancárias
            [5] Depósito
            [6] Saque
            [7] Extrato
            [8] Cancelar
    \n\n
    """


def show_transaction_history_value(balance_value):
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


def show_deposit_transactions_in_day_number(deposit_in_day_number):
    if deposit_in_day_number > 0:
        print("Depósitos realizados no dia:", deposit_in_day_number)
    else:
        print("Não foram realizados depósitos no dia de hoje")

    return deposit_in_day_number


def show_transactions_in_day_number(
    transactions_in_day_number, transactions_per_day_limit
):
    if transactions_in_day_number > 0:
        if transactions_in_day_number < transactions_per_day_limit:
            print(
                f"Transações realizadas no dia: {transactions_in_day_number}/{transactions_per_day_limit}"
            )
        else:
            print(
                f"O limite de {transactions_per_day_limit} transações diárias foi batido! "
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
    withdrawal_transaction_value,
    withdrawal_per_operation_limit_value,
    balance_value,
):
    if (
        withdrawal_transaction_value > 0
        and withdrawal_transaction_value <= balance_value
        and withdrawal_transaction_value <= withdrawal_per_operation_limit_value
    ):
        return True
    else:
        return False


def withdrawal_transactions_in_day_limit_verify(
    transaction_date_time,
    withdrawal_transaction_per_day_limit_number,
    withdrawal_transaction_in_day_number,
):
    today = get_date_now()

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
            if transactions_in_day_number < transactions_per_day_limit:
                return True
            else:
                return False
    else:
        print("Não é possível realizar agendas de transações, cancelando operação...")
        return False


def user_registry(users):
    print("\nOpção REGISTRO de usuários selecionada...")

    user_name = str(input("Informe o nome:"))
    user_birtdate = str(input("Informe a data de nascimento:"))
    user_cpf = int(input("Informe o CPF - números:"))
    user_street = str(input("Informe a rua:"))
    user_street_number = str(input("Informe o número:"))
    user_neighborhood = str(input("Informe o bairro:"))
    user_city = str(input("Informe a cidade:"))
    user_state = str(input("Informe o estado - sigla:"))

    if user_verify_cpf(users, user_cpf) is False:
        users.append(
            dict(
                name=user_name,
                birtdate=user_birtdate,
                cpf=user_cpf,
                adress=f"{user_street}, {user_street_number} - {user_neighborhood} - {user_city}/{user_state}",
                accounts=[],
            )
        )

        print("Usuário cadastrado com sucesso!")
    else:
        print("CPF já cadastrado.")

    return users


def user_verify_cpf(users, cpf):
    return any(user["cpf"] == cpf for user in users)  # Usando any para simplificar


def account_registry(users, accounts, account_number_prefix):
    user_cpf = int(input("Informe o CPF do usuário:"))

    user = next((user for user in users if str(user["cpf"]) == str(user_cpf)), None)

    if user is None:
        print("Usuário não encontrado.")
        return accounts
    else:
        if "accounts" not in user:
            user["accounts"] = []

        account_number = str(input("Informe o número da conta:"))
        account_number = str(account_number_prefix) + str(account_number)

        user["accounts"].append(account_number)
        accounts.append(
            dict(
                cpf=user_cpf,
                agency=account_agency,
                number=account_number,
            )
        )

        account_number_prefix += 1
        print("Conta cadastrada com sucesso!")

        return accounts, account_number_prefix


def show_transaction_confirmation_message(transaction_value, transaction_type_name):
    return print(
        f"O valor de {transaction_value} foi {transaction_type_name} com sucesso!"
    )


def print_values(values):
    if values:
        for value in values:
            print(f"\n", value)


while option != 0:
    print(show_menu())
    option = int(input("Opção escolhida:"))
    if option == 1:
        users = user_registry(users)
    elif option == 2:
        print_values(users)
    elif option == 3:
        accounts, account_number_prefix = account_registry(
            users, accounts, account_number_prefix
        )
    elif option == 4:
        print_values(accounts)
    elif option == 5:
        user_cpf = input("Informe seu CPF: ")  # Adicionando captura do CPF do usuário
        (
            balance_value,
            deposit_in_day_number,
            transactions_in_day_number,
            transactions_history,
        ) = deposit_transaction_value(
            balance_value,
            deposit_in_day_number,
            transactions_in_day_number,
            transactions_per_day_limit,
            transactions_history,
            user_cpf,  # Passando CPF do usuário
        )
    elif option == 6:
        user_cpf = input("Informe seu CPF: ")  # Adicionando captura do CPF do usuário
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
            user_cpf,  # Passando CPF do usuário
        )
    elif option == 7:
        show_transaction_history(
            balance_value,
            withdrawal_transaction_in_day_number,
            withdrawal_transaction_per_day_limit_number,
            deposit_in_day_number,
            transactions_in_day_number,
            transactions_history,
            user_cpf,
        )
    elif option == 8:
        print("Operação cancelada.")
    else:
        print("Opção inválida! Tente novamente.")

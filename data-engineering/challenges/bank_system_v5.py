from datetime import datetime


class Account:
    def __init__(
        self, cpf, agency, number, balance_value, withdrawal_limit, transactions_limit
    ):
        self.cpf = cpf
        self.agency = agency
        self.number = number
        self.balance_value = balance_value
        self.withdrawal_limit = withdrawal_limit
        self.transactions_limit = transactions_limit
        self.transactions_in_day_number = 0
        self.withdrawal_transactions_in_day_number = 0
        self.deposit_in_day_number = 0
        self.transactions_history = ""

    def __str__(self):
        return (
            f"Conta número: {self.number} | Agência: {self.agency} | "
            f"Saldo: R$ {self.balance_value} | CPF do Titular: {self.cpf}"
        )

    def deposit(self, amount):
        if amount > 0:
            self.balance_value += amount
            self.deposit_in_day_number += 1
            self.transactions_in_day_number += 1
            self.transactions_history = self.update_transaction_history(
                amount, "depositado"
            )
            return True
        return False

    def withdraw(self, amount, withdrawal_per_operation_limit_value):
        if (
            0 < amount <= self.balance_value
            and amount <= withdrawal_per_operation_limit_value
        ):
            self.balance_value -= amount
            self.withdrawal_transactions_in_day_number += 1
            self.transactions_in_day_number += 1
            self.transactions_history = self.update_transaction_history(
                amount, "sacado"
            )
            return True
        return False

    def update_transaction_history(self, amount, transaction_type):
        transaction_date_time = datetime.now()
        history_entry = f"\nDia: {transaction_date_time.date()} | Hora: {transaction_date_time.time()} | O valor de R$ {amount} foi {transaction_type}."
        self.transactions_history += history_entry
        return self.transactions_history


class User:
    def __init__(self, name, birthdate, cpf, address):
        self.name = name
        self.birthdate = birthdate
        self.cpf = cpf
        self.address = address
        self.accounts = []

    def __str__(self):
        return f"Nome: {self.name} | CPF: {self.cpf} | Endereço: {self.address}"

    def add_account(self, account):
        self.accounts.append(account)


class BankSystem:
    def __init__(self):
        self.users = []
        self.accounts = []

    def validate_cpf(self, cpf):
        return len(cpf) == 11 and cpf.isdigit()

    def get_user_by_cpf(self, cpf):
        return next((user for user in self.users if user.cpf == cpf), None)

    def get_accounts_by_user_cpf(self, cpf):
        return [account for account in self.accounts if account.cpf == cpf]

    def get_account_by_number(self, number):
        return next(
            (account for account in self.accounts if account.number == number), None
        )

    def register_user(self, name, birthdate, cpf, address):
        if not self.validate_cpf(cpf):
            print("CPF inválido.")
            return False
        if self.get_user_by_cpf(cpf):
            print("CPF já cadastrado.")
            return False

        new_user = User(name, birthdate, cpf, address)
        self.users.append(new_user)
        print(f"Usuário {name} cadastrado com sucesso.")
        return True

    def register_account(
        self, user_cpf, agency, balance_value, withdrawal_limit, transactions_limit
    ):
        user = self.get_user_by_cpf(user_cpf)
        if user:
            account_number = (
                f"{len(self.accounts) + 1:010d}"  # Gera um número de conta único
            )
            new_account = Account(
                user_cpf,
                agency,
                account_number,
                balance_value,
                withdrawal_limit,
                transactions_limit,
            )
            user.add_account(new_account)
            self.accounts.append(new_account)
            print(
                f"Conta número {new_account.number} | agência {new_account.agency} para {user.name} cadastrada com sucesso."
            )
        else:
            print("Usuário não encontrado.")

    def deposite_value(self, account_number, value):
        account = self.get_account_by_number(account_number)
        if account and value > 0:
            account.deposit(value)
            print(f"Depósito de R$ {value} realizado com sucesso.")
        else:
            print("Conta não encontrada ou valor inválido.")

    def withdrawal_value(self, account_number, value):
        account = self.get_account_by_number(account_number)
        if account and value > 0:
            account.withdraw(value, account.withdrawal_limit)
            print(f"Saque de R$ {value} realizado com sucesso.")
        else:
            print("Conta não encontrada ou valor inválido.")

    def show_users(self):
        users = self.users
        if users:
            print_values(users)

    def show_user_accounts(self, cpf):
        user = self.get_user_by_cpf(cpf)
        if user:
            accounts = self.get_accounts_by_user_cpf(cpf)
            print_values(accounts)
        else:
            print("Usuário não encontrado.")

    def show_account_statement(self, user_cpf):
        accounts = self.get_accounts_by_user_cpf(user_cpf)
        if accounts:
            for account in accounts:
                print("\n########### Extrato de conta ###########")
                print(f"CPF: {account.cpf}")
                print(f"Saldo: R$ {account.balance_value}")
                print(f"Histórico de transações: {account.transactions_history}")
                print(
                    f"Transações no dia: {account.transactions_in_day_number}/{account.transactions_limit}"
                )
                print(
                    f"Saques no dia: {account.withdrawal_transactions_in_day_number}/{account.withdrawal_limit}"
                )
                print(f"Depósitos no dia: {account.deposit_in_day_number}")
                print("########################################\n")
        else:
            print("Conta não encontrada.")


def print_values(values):
    if values:
        for value in values:
            print(f"\n{value}")


# Sistema bancário inicializado
bank_system = BankSystem()


# Menu original
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


# Exemplo de uso
def main():
    bank_system.register_user(
        "Sabrina B. M.", "26/01/1994", "08524655992", "Rua bonita, 564"
    )
    bank_system.register_user("Et Bilu", "10/10/201", "00000000000", "Via láctea, 035")
    while True:
        option = int(input(show_menu()))
        if option == 1:
            name = input("Nome: ")
            birthdate = input("Data de Nascimento (dd/mm/yyyy): ")
            cpf = input("CPF (somente números): ")
            address = input("Endereço: ")
            bank_system.register_user(name, birthdate, cpf, address)
        elif option == 2:
            print_values(bank_system.users)
        elif option == 3:
            cpf = input("CPF (somente números): ")
            bank_system.register_account(cpf, 1, 0, 3, 10)
        elif option == 4:
            cpf = input("CPF (somente números): ")
            print_values(bank_system.show_user_accounts(cpf))
        elif option == 5:
            account_number = input("Número da conta (somente números): ")
            value = float(input("Valor para depósito: "))
            bank_system.deposite_value(account_number, value)
        elif option == 6:
            account_number = input("Número da conta (somente números): ")
            value = float(input("Valor para saque: "))
            bank_system.withdrawal_value(account_number, value)
        elif option == 7:
            account_number = input("Número da conta (somente números): ")
            bank_system.show_account_statement(account_number)
        elif option == 8:
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()

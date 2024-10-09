from datetime import datetime, date
from abc import ABC, abstractmethod
import random


# Classe base Person
class Person:
    def __init__(self, cpf, name, birthdate):
        self.cpf: str = cpf
        self.name: str = name
        self.birthdate: date = birthdate


class Client(Person):
    def __init__(self, cpf, name, birthdate, address):
        super().__init__(cpf, name, birthdate)
        self.address: str = address
        self.accounts: list = []

    def add_account(self, account):
        self.accounts.append(account)
        return self.accounts

    def get_account_by_number(self, account_number):
        return next(
            (acc for acc in self.accounts if acc.account_number == account_number), None
        )

    @classmethod
    def transaction(cls, account_number, transaction):
        account = get_account_by_number(account_number)
        if account:
            account.historic.add_transaction(account, transaction)
            return account
        return None

    def show_transactions(cls, account_number):
        account = get_account_by_number(account_number)
        if account:
            return account.historic.show_transactions(account)
        return None

    # Retorno da função de print de usuários
    def __str__(self):
        return f"\nCliente: {self.name}, CPF: {self.cpf}, Endereço: {self.address}, Data de Nascimento: {self.birthdate}"


class Transaction(ABC):
    @abstractmethod
    def register_account(self, cpf_user, account_number):
        pass

    @abstractmethod
    def withdrawal(self, value: float):
        pass

    @abstractmethod
    def deposit(self, value: float):
        pass


class Account(Transaction):
    def __init__(self, balance, account_agency_number, account_number, client):
        self.balance: float = balance
        self.account_agency_number: str = account_agency_number
        self.account_number: int = account_number
        self.client: Client = client
        self.historic: Historic = Historic(self)
        self.withdrawal_value_limit: float = 500  # limitador de valor por saque
        self.withdrawal_limit_day: int = 3  # limitador de quantidade de saques diários
        self.withdrawal_today: int = 0  # Contador de quantidade de saques diários
        self.transactions_today: int = 0  # Contador de quantidade de transações diárias
        self.transactions_daily_limit: int = 10  # limitador de transações diárias

    def register_account(self, cpf_user, account_number):
        pass

    def withdrawal(self, value: float):
        # Validações de limites para operação
        # limite de saque
        if self.withdrawal_today >= self.withdrawal_limit_day:
            return print(
                f"Limite diário de saques de {self.withdrawal_limit_day} já foi alcançado!"
            )

        # limite de transações
        if self.transactions_today >= self.transactions_daily_limit:
            return print(
                f"Limite de {self.transactions_daily_limit} transações diárias alcançado!"
            )

        # Validação de valores para operação
        # validação de valor limite de saque
        if value > self.withdrawal_value_limit:
            return print(
                f"Valor de {value} é maior que o limite de {self.withdrawal_value_limit} permitido para operação!"
            )

        # validação de valor da operação
        if value > 0 and value <= self.balance:
            self.balance -= value
            self.withdrawal_today += 1
            self.transactions_today += 1
            self.historic.add_transaction(
                f"Saque de R$ {value} | Saldo Atual: R$ {self.balance}"
            )
            print(f"Saque de R$ {value} | Saldo Atual: R$ {self.balance}")
            return self.balance

        else:
            return print(f"Valor informado de {value} inválido!")

    def deposit(self, value: float):
        # limite de transações
        if self.transactions_today >= self.transactions_daily_limit:
            return print(
                f"Limite de {self.transactions_daily_limit} transações diárias alcançado!"
            )

        # validação de valor da operação
        if value > 0:
            self.balance += value
            self.transactions_today += 1
            self.historic.add_transaction(
                f"Depósito de R$ {value} | Saldo Atual: R$ {self.balance}"
            )
            print(f"Depósito de R$ {value} | Saldo Atual: R$ {self.balance}")
            return self.show_balance()
        else:
            return print(f"Valor informado de {value} inválido!")

    def show_balance(self):
        return self.balance

    def show_account_statement(self):
        print(
            f"\nNúmero: Agência {self.account_agency_number} | Conta {self.account_number}"
        )
        print(f"CPF: {self.client.cpf}")
        print(f"Saldo: R$ {self.balance}")
        print(f"Histórico de transações:")
        self.historic.show_transactions()
        print(
            f"Limites diários: Transações {self.transactions_today} | Saques {self.withdrawal_today}/{self.withdrawal_limit_day}"
        )
        print("########################################\n")

    @classmethod
    def new_account(
        cls,
        client: Client,
        account_agency_number: int,
        account_number: int,
    ):
        return cls(0, account_agency_number, account_number, client)

    # Retorno da função de print de contas
    def __str__(self):
        return f"\nCliente: {self.client.name}, CPF: {self.client.cpf} | Conta agência: {self.account_agency_number} número: {self.account_number}, saldo: {self.balance}"


class Historic:
    def __init__(self, account):
        self.account: Account = account
        self.transactions: list = []

    # Adiciona uma transação ao histórico
    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def show_transactions(self):
        print_values(self.transactions)

    def __str__(self):
        return "\n".join(self.transactions)


class BankSystem:
    def __init__(self):
        self.users = []
        self.accounts = []

    def validate_cpf(self, cpf):
        return len(cpf) == 11 and cpf.isdigit()

    def get_user_by_cpf(self, cpf):
        return next((user for user in self.users if user.cpf == cpf), None)

    def get_accounts_by_user_cpf(self, cpf):
        return [account for account in self.accounts if account.client.cpf == cpf]

    def get_account_by_number(self, account_number):
        for account in self.accounts:
            if int(account.account_number) == int(account_number):
                return account

    def get_next_account_number(self, client):
        # Garante que o número da conta seja incremental e sequencial para o cliente
        new_account_prefix = 1
        new_account_sufix = (
            str(random.randint(0, 9))
            + str(random.randint(0, 9))
            + str(random.randint(0, 9))
        )
        accounts = [acc for acc in self.accounts if acc.client == client]
        if accounts:
            new_account_prefix: int = new_account_prefix + 1
        return str(new_account_prefix) + str(new_account_sufix)

    def register_user(self, name, birthdate, cpf, address):
        if not self.validate_cpf(cpf):
            print("CPF inválido.")
            return False
        if self.get_user_by_cpf(cpf):
            print("CPF já cadastrado.")
            return False

        new_user = Client(cpf, name, birthdate, address)
        self.users.append(new_user)
        print(f"Usuário {name} cadastrado com sucesso.")
        return True

    def register_account(self, user_cpf):
        user = self.get_user_by_cpf(user_cpf)
        if user:
            account_number = self.get_next_account_number(user)
            new_account = Account(0, "001", account_number, user)
            user.add_account(new_account)
            self.accounts.append(new_account)
            print(
                f"\nConta número {new_account.account_number} para {user.name} cadastrada com sucesso."
            )
        else:
            print(f"\nUsuário com cpf {user_cpf} não cadastrado.")

    def deposit_value(self, account_number, value):
        account = self.get_account_by_number(account_number)
        if account:
            return account.deposit(value)
        else:
            print(f"Conta número {account_number} não encontrada!")

    def withdrawal_value(self, account_number, value):
        account = self.get_account_by_number(account_number)
        if account:
            return account.withdrawal(value)
        else:
            print(f"Conta número {account_number} não encontrada!")

    def show_account_statement(self, user_cpf):
        accounts = self.get_accounts_by_user_cpf(user_cpf)
        if accounts:
            for account in accounts:
                print(f"\n########### Extrato de conta ###########")
                print(
                    f"Número: Agência {account.account_agency_number} | Conta {account.account_number}"
                )
                print(f"CPF: {account.client.cpf}")
                print(f"Saldo: R$ {account.balance}")
                print(f"Histórico de transações:")
                account.historic.show_transactions()
                print(
                    f"Limites diários: Transações {account.transactions_today} | Saques {account.withdrawal_today}/{account.withdrawal_limit_day}"
                )
                print("########################################\n")
        else:
            print("Conta não encontrada.")


def print_values(values):
    if values:
        for value in values:
            print(f"{value}")


def main():
    bank_system = BankSystem()
    bank_system.register_user(
        "Sabrina B. M.", "26/01/1994", "11111111111", "Rua bonita, 564"
    )
    bank_system.register_user("Et Bilu", "10/10/2010", "00000000000", "Via Láctea, 035")
    bank_system.register_account("11111111111")
    bank_system.register_account("11111111111")

    while True:
        option = int(input(show_menu()))
        if option == 1:  # cadastrar usuários
            name = input("Nome: ")
            birthdate = input("Data de Nascimento (dd/mm/yyyy): ")
            cpf = input("CPF (somente números): ")
            address = input("Endereço: ")
            bank_system.register_user(name, birthdate, cpf, address)
            print("\n")
        elif option == 2:  # listar usuários
            print_values(bank_system.users)
            print("\n")
        elif option == 3:  # registrar conta
            cpf = input("CPF do cliente (somente números): ")
            account_number = input("Número da conta (somente números): ")
            bank_system.register_account(account_number)
            print("\n")
        elif option == 4:  # listar contas
            cpf = input("CPF do cliente (somente números): ")
            bank_system.show_account_statement(cpf)
            print("\n")
        elif option == 5:  # deposito
            account_number = int(input("Número da conta: "))
            value = float(input("Valor para depósito: "))
            bank_system.deposit_value(account_number, value)
            print("\n")
        elif option == 6:  # saque
            account_number = int(input("Número da conta (somente números): "))
            value = float(input("Valor para saque: "))
            bank_system.withdrawal_value(account_number, value)
            print("\n")
        elif option == 7:  # extrato de contas
            cpf = input("CPF (somente números): ")
            bank_system.show_account_statement(cpf)
            print("\n")


def show_menu():
    return (
        "\n########## MENU #########\n"
        "Selecione a sua ação:\n"
        "1. Registrar novo cliente\n"
        "2. Mostrar lista de clientes\n"
        "3. Registrar nova conta bancária\n"
        "4. Mostrar contas do cliente\n"
        "5. Depositar valor\n"
        "6. Sacar valor\n"
        "7. Exibir extrato de contas\n"
        "8. Sair\n"
        "Escolha uma opção: "
    )


if __name__ == "__main__":
    main()

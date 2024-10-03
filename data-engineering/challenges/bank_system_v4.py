from abc import ABC, abstractmethod


class Person:
    def __init__(self):
        self.cpf: str = (cpf,)
        self.name: str = (name,)
        self.birthdate: date = birthdate


class Client(Person):
    def __init__(self):
        self.address: str = address
        self.accounts: Account = accounts

    @classmethod
    def transaction(cls, account, transaction):
        account_to_transaction = any(
            user_account.number == account.number for user_account in cls.accounts
        )
        print(f"account_to_transaction: {account_to_transaction}")
        cls.accounts[account_to_transaction.number].historic = cls.accounts[
            account_to_transaction.number
        ].historic.append(transaction)
        return cls.account

    @classmethod
    def add_account(cls, account):
        self.accounts = self.accounts.append(account)
        return self.accounts


class Transaction(ABC):
    @abstractmethod
    def registry(self, account):
        pass

    @abstractmethod
    def withdrawal(self, value: float):
        pass

    @abstractmethod
    def deposity(self, value: float):
        pass


class Account(Transaction):
    def __init__(self):
        self.balance: float = (balance,)
        self.account_number: int = (account_number,)
        self.account_agency_number: str = (account_agency_number,)
        self.client: Client = client
        self.Historic: Historic = Historic

    @classmethod
    def show_balance(cls):
        return cls.balance

    @classmethod
    def withdrawal(cls, value: float):
        if value < 0:
            cls.balance -= value
            return cls.balance

    @classmethod
    def deposity(cls, value: float):
        if value < 0:
            cls.balance += value
            return cls.balance

    @classmethod
    def new_account(
        cls, client: Client, account_number: int, account_agency_number: int
    ):
        new_account = Account(
            0, account_number, account_agency_number, client, Historic()
        )
        return new_account


class Account_corrent(Account):
    def __init__(self):
        self.daily_limit_value_to_withdrawal: float = (500,)
        self.daily_limit_number_to_withdrawal: int = (3,)


class Historic:
    def __init__(self, account, transaction):
        self.account: Account = (account,)
        self.transaction: Transaction = transaction

    @classmethod
    def add_transaction(cls, account, transaction):
        return account.historic.append(Historic(transaction))

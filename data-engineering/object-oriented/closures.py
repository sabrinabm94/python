class Conta:
    def __init__(self, numero_agencia: int = 0, saldo=0):
        self.numero_agencia = numero_agencia
        self._saldo = saldo
        self.__novo_saldo = (
            saldo  # Atributo privado com nome diferente para evitar colisão
        )

    def depositar(self, valor):
        pass

    def sacar(self, valor):
        pass

    def mostrar_saldo(self):
        return self._novo_saldo

    # Criação da propriedade _novo_saldo
    @property
    def _novo_saldo(self):
        return self.__novo_saldo + 1 or 0  # Acesso ao atributo privado __novo_saldo

    @_novo_saldo.setter
    def _novo_saldo(self, valor):
        self.__novo_saldo = (
            self.__novo_saldo + valor
        )  # Atualiza o valor somando ao saldo atual

    @_novo_saldo.deleter
    def _novo_saldo(self):
        self.__novo_saldo = -1  # Define o saldo como -1 quando deletado


# Exemplo de uso
conta = Conta(1, 100)

# por convenção, não deveria manipular ou acessar a variável privada .__novo_saldo fora do escopo da classe
print(conta._saldo)
print(f"_novo_saldo inicial: {conta._novo_saldo}")
conta._novo_saldo = 5
print(f"_novo_saldo alterado: {conta._novo_saldo}")
del conta._novo_saldo
print(f"_novo_saldo deletado: {conta._novo_saldo}")

# para acessar variáveis privadas fora da classe, deverá ser via método get da propriedade desejada
print(f"_novo_saldo valor: {conta.mostrar_saldo()}")

# somente variáveis públicas
print(f"Agencia: {conta.numero_agencia}")

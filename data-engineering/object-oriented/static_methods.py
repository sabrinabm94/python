# Método estático
# Método vinculado a classe que não recebe o primeiro argumento explícito.
# Não acessa ou modifica a classe, diferente do método da classe que altera e tem o primeiro parametro como explícito.
# O método da classe é chamado de método de fábrica por criar as instancias da classe
# O método estático geralmente é usado para métodos utilitários


class Person:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    # Por ser um método de classe, trocamos o self por cls
    @classmethod
    def create_by_birth_date(cls, year, month, name):
        age = 2024 - year
        return cls(name, age)

    @staticmethod
    def above_age(age):
        return age >= 18


sabrina = Person("Sabrina", 30)
print(sabrina.name)

# Chamando método de classe
print("\n Builder método create_by_birth_date()")
yuki = Person.create_by_birth_date(2019, 1, "Yuki")
print(yuki.name, yuki.age)

# Chamando método estático
print("\n Static método above_age():")
print(Person.above_age(yuki.age))

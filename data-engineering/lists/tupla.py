# Tupla
# É similar a listas, mas seus valores são imutáveis, ou seja, seus valores são atribuidos na criação e até o fim do programa não podem ser alterados e serão os mesmos da declaração.

colors = ("Branco", "Preto", "Cinza")
print("\nColors: ", colors)

# Matriz

matrix = (
    (1, 2),
    ("a", "b"),
)

print("\nMatriz: ", matrix[0][1], matrix[1][0])

# Tuple
# Método para converter valores em uma tupla
numbers = tuple([1, 2, 3])
print("\nNumbers: ", numbers)

name = tuple("Sabrina")
print("\nName: ", name)

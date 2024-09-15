# listas
# Aceitam variados tipos de valores
list = ["Sabrina", 30, 30, ["Hedera helix", "Epipremnum aureum"]]
print("\nList: :", list)

for index, list_item in enumerate(list):
    print(index, list_item)

# Matris
# Listas multiciomencionais
matrix = (
    ["Verde", "Amarelo", "Laranja"],
    ["Vermelho", "Roxo"],
    ["Cinza", "Preto", "Ciano"],
)
print("\nMatris: ", matrix[0][0], matrix[1][1], matrix[2][2])

# Métodos para listas

# Copy
# Duplica uma lista existente
coppied_list = list.copy()
print("\ncoppied_list - copy: ", coppied_list)

# Append
# Adiciona um valor único ao final da listagem
coppied_list.append(["Hedera helix", "Epipremnum aureum", "Vanilla planifolia"])
print("\ncoppied_list - append: ", coppied_list)

# Count
# Conta quantas vezes um valor aparece na listagem
print("\ncoppied_list - count: ", coppied_list.count(30))

# Extend
# Adiciona multiplos valores ao final de lista
list.extend(["Não é Epipremnum aureum", "é Vanilla planifolia"])
print("\nlist - extend: ", list)

# Index
# Busca um valor na lista e retorna o seu index, se tiver mais de um valor igual, retorna o primeiro encontrado
print("\nlist - index: ", list.index(30))

# Pop
# Remove o último elemento da listagem
list.pop()
print("\nlist - pop: ", list)

list.pop()
print("list - pop: ", list)

# Remove
# Remove um elemento da lista baseado no seu valor, remove o primeiro encontrado
list.remove(30)
print("\nlist - remove: ", list)

# Reverse
# Reorganiza a lista invertendo sua ordem
numbers = [1, 2, 3]
print("\nnumbers: ", numbers)
numbers.reverse()
print("\nnumbers - reverse: ", numbers)

# Sort
# Reorganiza uma listagem baseado em parametros

names = ["Ana", "Anne", "Rebeka", "Katarine", "Sabrina", "Bonnie", "Klaus"]
print("\nNames: ", names)

# Recuperando valores da lista pelo index
# Index positivo
# Primeiro valor
print("Names [0]: ", names[0])
print("Names [3]: ", names[3])

# Index negativo
# Último valor
print("Names [-1]: ", names[-1])
print("Names [-3]: ", names[-3])

names.sort()
print("\nNames - sort: ", names)

names.sort(reverse=True)
print("Names - reverse: ", names)

# Função lambda: organizar por tamanho dos valores - ascendente
names.sort(key=lambda x: len(x))
print("\nNames - lambda values sizes: ", names)

# Função lambda: organizar por tamanho dos valores - descendente
names.sort(key=lambda x: len(x), reverse=True)
print("Names - lambda values sizes reverse: ", names)

# Sets
# coleção de objetos não repetidos, usado para retirar itens duplicados de iteráveis

numbers = [1, 2, 2, 3, 4, 5, 33]
print("numbers: ", numbers)

numbers = set(numbers)
print("numbers - set: ", numbers)

numbers = sorted(set(numbers))
print("numbers - set sorted: ", numbers)

# Conjuntos
# Union
first_set = set([1, 2, 3])
second_set = set([4, 5, 6])

union = first_set.union(second_set)
print("\nUnion: ", union)

# Intersecção
name = set(["Sabrina", "Boing", "Moreira"])
lastname = set(["B.", "Moreira"])

intersection = name.intersection(lastname)
print("\nintersection : ", intersection)

# Diferença
# Retorna a diferença do primeiro conjunto comparado
difference = name.difference(lastname)
print(f"\ndifference: {name} x {lastname} \n", difference)

# Diferença simétrica
# Retorna as diferenças em todos os objetos comparados
symmetric_difference = name.symmetric_difference(lastname)
print(f"\nsymmetric_difference: {name} x {lastname} \n", symmetric_difference)

# add
# Adiciona um elemento se ele nao existir no conjunto
third_set = set([1])
third_set.add(3)
print("third_set: ", third_set)

# issuperset
issupersetVerification = first_set.issuperset(third_set)
print(f"\n {first_set} is superset {third_set}: ", issupersetVerification)

# issubset
issubsetVerification = third_set.issubset(second_set)
print(f"\n{third_set} is subset {second_set}: ", issubsetVerification)

# isdisjoint
# Verifica se os conjuntos sâo totalmente diferentes
isdisjointVerification = second_set.isdisjoint(third_set)
print(f"\n {second_set} is dis joint {third_set}: ", isdisjointVerification)
print(f"\n {first_set} is dis joint {third_set}: ", first_set.isdisjoint(third_set))


# copy
# Retorna uma conjunto copiado de outro
coppied_set = third_set.copy()
print("coppied_set: ", coppied_set)

# discart
# Remove o valor indicado do conjunto
print("second_set: ", second_set)
second_set.discard(5)
second_set.discard(100)
print("discard value 5 and 100: ", second_set)

# pop
# Remove o primeiro valor de um conjunto
print("first_set: ", first_set)
first_set.pop()
print("pop: ", first_set)

# remove
# Remove o valor indicado do conjunto e caso não exista o elemento para remover, causa erro
print("third_set: ", third_set)
third_set.remove(1)
print("remove value 1: ", third_set)

# in
# Verifica se o valor se encontra no conjunto indicado
print(f"3 in {third_set}: ", 3.0 in (third_set))
print(f"100 in {third_set}: ", 100 in (third_set))

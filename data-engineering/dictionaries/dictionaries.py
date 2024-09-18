# Dicionários
# Conjunto não ordenado de dados com chave e valor

sabrina = {"name": "Sabrina", "age": 16, "color": "lilac"}
cats = dict(name="Luna", age=3)
cats["plays"] = "Jump in the doors"
cats["sister"] = dict(name="Yuki", age=1, plays="Run in the house")

print("\n sabrina: ", sabrina)
print("\n cats: ", cats)

# Loops
print("\nLoops")

for key, value in cats.items():
    print(f"{key}: ", value)

# Copy
# retorna um novo dicionário copiado a partir de outro
sara = dict(sabrina.copy())
sara["name"] = "Sara"
print("\n sara: ", sara)

# Clear
# Apaga todos os valores de um dicionário
sabrina.clear()
print("\n sabrina: ", sabrina)

sara.fromkeys(["phone"], "123")
print("\n sara: ", sara)

# Get
# Obtem valores do dicionário
print("\n sara age: ", sara.get("age"))

print("\n sara favorite color: ", sara.get("color"), {})

# Itens
# Retorna os valores do dicionário como uma tupla
print("\n cats items: ", cats.items())

cats = dict(cats)
# Keys
# Retorna só as chaves de um dicionário
print("\n cats keys: ", cats.keys())

# Pop
# Retorna um novo dicionado com o valor removido pela sua chave, retornando o valor da chave removida
sara = sara.pop("amarelo", "Não encontrado")
sabrina = sabrina.pop("age", {})
print("\n sara: ", sara)
print("\n sabrina: ", sabrina)

# Pop items
# Retira um valor do dicionario retornando uma tupla
cats.popitem()
print("\n cats: ", cats)

# Set default
# Caso tenha a chave com valor, nada é alterado
# Caso não tenha a chave informada, adiciona ela com o seu valor
cats.setdefault("phone", "1234")
cats.setdefault("name", "sun")
print("cats: ", cats)

STRING_IN_LOWER_CASE = "sabrina"

# Case
print("\nCase")
print("Uppercase: ", STRING_IN_LOWER_CASE.upper())
print("lowercase:", STRING_IN_LOWER_CASE.lower)
print("First letter to upercase", STRING_IN_LOWER_CASE.title())

# Spaces
print("\nSpaces")
STRING_WITH_SPACE = "    some string    "
print("Original string:", STRING_WITH_SPACE)
print("Remove all spaces:", STRING_WITH_SPACE.strip() + ".")
print("Remove left spaces:", STRING_WITH_SPACE.lstrip() + ".")
print("Remove right spaces:", STRING_WITH_SPACE.rstrip() + ".")


# Centralization
STRING_TO_CENTERLIZE = "Python"
print("\nCentralization")
print("####", STRING_TO_CENTERLIZE, "####")  # string com espaços com ,
print("####" + STRING_TO_CENTERLIZE + "####")  # string sem espaços com +
print(
    STRING_TO_CENTERLIZE.center(14, "#")
)  # apresentação de string centralizada com metade de 14 caracteres em cada lado

# Join
print("\nJoin")
print("p-y-t-h-o-n")
print("-".join(STRING_TO_CENTERLIZE))


# Interpolação
print("\nInterpolation")

# old file
name = "Sabrina"
age = 30
profission = "Developer"
language = "Python"
print(
    "OLD FILE: Eu sou %s e tenho %d de idade, trabalho como %s e faço o curso de %s."
    % (name, age, profission, language)
)

# format
print(
    "FORMAT: Eu sou {} e tenho {} de idade, trabalho como {} e faço o curso de {}.".format(
        name, age, profission, language
    )
)

print(
    "FORMAT: Eu sou {name} e tenho {age} de idade, trabalho como {profission} e faço o curso de {language}".format(
        name="Eduardo", age=20, profission=profission, language="Lua"
    )
)

# f-string
print(
    f"F-STRING: Eu sou {name} e tenho {age} de idade, trabalho como {profission} e faço o curso de {language}"
)

print("\nFLOAT FORMATION")
PI = 3.14159
print(f"Valor de PI: {PI:.1f}")
print(f"Valor de PI: {PI:10.2f}")

print("\nSTRING CUTTING")
# Um caracter
print("name[0]: ", name[0])
print("name[2]: ", name[2])

# Uma faixa de caracteres
print("name[0:2]: ", name[0:2])
print("name[2:]: ", name[2:])

# Um trecho saltando pelo step
print("name[0:5:2]: ", name[0:5:2])

# Completo
print("name[:] ", name[:])

# Inversão
print("name[::-1] ", name[::-1])

# Aspas trilhas
# Preserva a formatação de seu conteúdo
message = f"""
  Olá o meu nome é
      Ciclano
    do Acre
"""
print(message)

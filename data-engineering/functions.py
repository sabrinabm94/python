# *args e **kwargs
# depois de usar o * todos os parametros da funçao aceitam somente parametros do tipo keywords
def new_car(*, brand, model, year, license_plate):
    print(
        f"Novo carro cadastrado! \nMarca: {brand}, modelo: {model}, ano: {year}, placa: {license_plate}\n"
    )


# chamada de função usando parametros por posição
new_car(model="Palio", brand="Brasileiro", year="1994", license_plate="BATECAVERNA1234")


# depois de usar a / todos os parametros seguintes da funçao aceitam parametros do tipo keywords e position
def update_car(brand, model, /, year, license_plate):
    print(
        f"Carro atualizado! \nMarca: {brand}, modelo: {model}, ano: {year}, placa: {license_plate}\n"
    )


# chamada de função usando parametros hibridos
update_car("uno", "fiat", "2019", license_plate="BATECAVERNA1243")


# quando queremos usar tuplas como argumentos de uma função, usamos *args para indicar, e quando queremos utilizar um dicionário, usamo9s **kwargs
def print_poem(data, *text, **other_info):
    main_text = "\n".join(text)
    text_complementation = "\n".join(
        [f"{key.title()}: {value}" for key, value in other_info.items()]
    )
    full_text = f"\nInício do poema: \n{data}\n{main_text}\n\n{text_complementation}"
    print(full_text)


print_poem(
    "2024",
    "Zen of python",
    "Beautiful is better than ugly",
    author="Tim Peters",
    year=1999,
)

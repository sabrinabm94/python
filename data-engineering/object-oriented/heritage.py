# Herança
# Reflete o relacionamento entre os objetos e permite reutilização de código por ser transitiva, atualizando os herdeiros ao mexer na classe herdada.

import vehicle


class Car(vehicle.Vehicle):
    pass


# Herança multipla
# Quando uma classe extende de várias classes pai, dizemos que ela tem herança multiplas
# Herda de carro que herda de veículo
class Eletric_car(Car):
    def bibi(self):
        print("Eletric car bibibi")

        # Para chamar o método da classe base (Vehicle), usamos super()
        # super().bibi()


print("\n")
caloi = vehicle.Vehicle("Bicicleta", "Vermelho", "Caloi", 1994, 5000)
caloi.bibi()
print(caloi.color)
print(caloi.info())
print(caloi.__str__())

print("\n")
uno_mile = Car("Carro", "Preto", "Fiat", 1980, 20000)
print(uno_mile)

print("\n")
tesla = Eletric_car("Carro", "Preto", "Tesla", 2020, 300000)
print(tesla)

# Bibi do eletric car
tesla.bibi()

# Bibi do vehicle
# vehicle.Vehicle.bibi(tesla)

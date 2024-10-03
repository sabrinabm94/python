# Polimorfismo
# Um objeto com muitas formas, podendo aceitar vários tipos de dados.

print(len("Sabrina"))
print(len([1, 2, 3]))


class Bird:
    def fly(self):
        print("Voando...")


class Pidgey(Bird):
    def fly(self):
        print("O Pidgey voa")
        super().fly()


class Spearow(Bird):
    def fly(self):
        print("O Spearow voa também")
        super().fly()


def fly_with_me(bird):
    bird.fly()


fly_with_me(Pidgey())
fly_with_me(Spearow())

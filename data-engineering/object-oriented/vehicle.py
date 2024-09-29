class Vehicle:
    def __init__(self, type, color, model, year, value):
        self.type = type
        self.color = color
        self.model = model
        self.year = year
        self.value = value

    def __del__(self):
        # Chamada de método destruidor, após seu uso, a classe não existirá mais
        print("Destruíndo a classe")

    def bibi(self):
        print("Vehicle Bibibi")

    def info(self):
        return f"{self.type}: {self.color}, {self.model}, {self.year}, {self.value}"

    def __str__(self):
        return f"{self.__class__.__name__}: {[f'{key}={value}'for key,value in self.__dict__.items()]}"

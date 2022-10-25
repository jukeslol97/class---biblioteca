class Animal():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor=cor


    def comer(self):
        print(f'O {self.nome} {self.cor} foi comer.')

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def miar(self):
        print(f'O {self.nome} {self.cor} foi miando...')

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def latir(self):
        print(f'O {self.nome} {self.cor} foi latindo...')


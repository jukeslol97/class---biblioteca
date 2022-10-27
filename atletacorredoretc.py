class Atleta():
    def __init__(self, peso, aposentado=False):
        self. peso = peso
        self.aposentado = aposentado



    def aquecer(self):
        print( 'está aquecendo.')

    def aposentar(self):
        print('aposentou-se com sucesso!')


class Corredor(Atleta):
    def __init__(self, correndo = False):
        self.correndo = correndo
    def correr(self):
        print('correndo.')

class Nadador(Atleta):
    def __init__(self, nadando = False):
        self.nadando = nadando
    def nadar(self):
        print('nadando.')

class Ciclista(Atleta):
    def __init__(self, pedalando = False):
        self.pedalando = pedalando
    def pedalar(self):
        print('pedalando.')

class Triatleta(Nadador, Corredor, Ciclista):
    def __init__(self, maratonando = False):
        self.maratonando = maratonando

    def maratonar(self):
        print('maratonando.')











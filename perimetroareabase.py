base = float(input('digite a area:'))
altura = float(input('digite a altura:'))

class Forma:


    def __init__(self, area, perimetro):
        self.area = area
        self.perimetro = perimetro

class Retangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def Calcperimetro (self):
        calc = (base*2) + (altura*2)
        print(f'o perimetro é: {calc}')

class Triangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def Calcareatriangulo (self):
        calc2 = (base*altura)/2
        print(f'a area do triângulo é: {calc2}')

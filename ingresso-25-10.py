class Ingresso:
    def __init__(self,valor):
        self.valor=valor
    def imprimeValor(self):
        print(f'o valor do ingresso normal é R${self.valor}')

class VIP(Ingresso):
    def imprimeValorVip(self,adicional):
        self.adicional=adicional
        return print(f'o valor do ingresso vip é R${self.valor+self.adicional}'
                     f' e o valor adicinel é R${self.adicional}')
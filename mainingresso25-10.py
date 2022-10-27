from digital import*

valor= float(input('digite o valor do ingresso normal:'))
valorA= float(input('digite o valor adicional do ingresso vip:'))
ticket1=VIP(valor)
ticket1.imprimeValor()
ticket1.imprimeValorVip(valorA)
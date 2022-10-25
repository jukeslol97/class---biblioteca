from datetime import datetime

class ContaBancaria:
    def __init__(self, nome, numero, tipo, saldo=0, status=False, limite=0):
         self.nome=nome
         self.numero=numero
         self.saldo=saldo
         self.tipo=tipo
         self.status=status
         self.limite_atual = limite
         self.limite = limite

    def ativacao (self):
        agora = datetime.now()
        data_formatada = agora.strftime(f"%d/%m/%Y ás %H:%M:%S")

        if self.status==False:
            print(f'Olá {self.nome}, a sua conta foi ativada com sucesso em: {data_formatada}')
            self.status=True
        else:
            print(f'a sua conta não pode ser ativada, pois ela já foi ativada anteriormente.')

    def desativar_conta (self):
        agora = datetime.now()
        data_formatada = agora.strftime(f"%d/%m/%Y ás %H:%M:%S")

        if self.status==True:
            print(f'Olá {self.nome}, a sua conta foi desativada com sucesso! em: {data_formatada}')
            self.status=False
        else:

            print(f'a sua conta não pode ser desativada, pois ela já fo desativada anteriormente.')



    def checar_saldo (self):
        if self.status==False:
            print(f'a sua conta está desativada, por favor, ative sua conta.')
        else:
            print(f'o saldo da sua conta é: {self.saldo}')

    def deposito(self, valor):
        agora = datetime.now()
        data_formatada = agora.strftime(f"%d/%m/%Y ás %H:%M:%S")
        if self.status==False:
            print(f'a sua conta está desativada, por favor, ative sua conta.')
        elif self.limite_atual < self.limite:
            self.limite_atual += valor
            sobra = self.limite_atual-self.limite
            self.saldo = self.saldo+sobra
            print(f'olá {self.nome} seu deposito foi realizado em: {data_formatada} com exito e foi reposto {sobra} no seu limite especial.')
        else:
            self.saldo=self.saldo+valor

    def saque(self, valor_saque):
        agora = datetime.now()
        data_formatada = agora.strftime(f"%d/%m/%Y ás %H:%M:%S")
        if self.status==False:
            print(f'a sua conta está desativada, por favor, ative sua conta.')
        elif valor_saque > self.saldo:
            uso_especial = valor_saque - self.saldo
            self.limite_atual = self.limite - uso_especial
            self.saldo -= self.saldo
            print(f'Olá {self.nome}, você utilizou {uso_especial} do seu limite especial em: {data_formatada}')

        else:
            self.saldo = self.saldo - valor_saque
            print(f' você sacou: {valor_saque} em: {data_formatada} seu limite agora é de: {self.limite}')

    def ativar_limite(self, valor):
        agora = datetime.now()
        data_formatada = agora.strftime(f"%d/%m/%Y ás %H:%M:%S")
        if self.status==False:
            print(f'a sua conta está desativada, por favor, ative sua conta.')
        else:
            self.limite_atual+=valor
            print(f'ola {self.nome} seu limite foi ativado com sucesso em: {data_formatada}')

    def checar_limite(self):
        if self.status == False:
            print(f'a sua conta está desativada, por favor, ative sua conta.')
        else:
            print(f'o saldo do seu limite especial é: {self.limite_atual}')



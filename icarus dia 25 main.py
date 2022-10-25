from biblioteca import ContaBancaria


p1 = ContaBancaria('Icarus Melo', 1275, 'ContaCorrente')

p1.ativacao()
p1.checar_saldo()
p1.deposito(float(input('digite o valor a ser depositado: ')))
p1.checar_saldo()
p1.ativar_limite(4000)
p1.checar_limite()
p1.saque(float(input('digite um valor pra ser sacado: ')))
p1.checar_saldo()
p1.checar_limite()
p1.deposito(float(input('digite o valor a ser depositado: ')))
p1.checar_saldo()
p1.checar_limite()



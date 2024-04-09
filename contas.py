
saldo :float = 0
limite = 500
LIMITE_SAQUE_DIARIO = 3
saques = []
depositos = []
operacoes = []
#extrato = {"Extrato": saques, "Deposito": depositos}

menu = """
Escolha uma opção

[d] Depositar
[s] Sacar
[e] Extrato
[s] Sair

"""

def saque(valor):
    global saldo, limite
    if valor <= saldo:
        if len(saques) < LIMITE_SAQUE_DIARIO:
            if valor <= limite:
                saldo -= valor
                saques.append(valor)
                operacoes.append(f'Saque no valor de R$ {valor:.2f}\n')
                return print("\nSaque efetuado com sucesso\n")
            else:
                return print("\nLimite do valor de saque atingido\n")
        else:
            return print("\nLimite de saques diarios atingido \n")
    else: 
        return print("\nNão foi possivel efetuar o saque\n")
    

def deposito(valor):
    global saldo
    if valor > 0:
        saldo += valor
        depositos.append(saldo)
        operacoes.append(f'Deposito no valor de R$ {valor:.2f}\n')
        return print("\nDeposito efetuado com sucesso\n")

def extrato():
    global saldo
    texto = '\n'
    for a in operacoes:
        texto += a
    texto += f'__________________\n'
    texto += f'O saldo Total é: R$ {saldo:.2f}\n'
    return print(texto)

while True:
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("\nInforme o valor a depositar\n"))
        deposito(valor)
    elif opcao == "s":
        valor = float(input("\nInforme o valor a sacar\n"))
        saque(valor)
    elif opcao == "e":
        extrato()
    elif opcao == "s":
        break
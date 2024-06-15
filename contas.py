saldo :float = 0
limite = 500
LIMITE_SAQUE_DIARIO = 3
operacoes = []
saques = 0
menu = """
Escolha uma opção

[d] Depositar
[s] Sacar
[e] Extrato
[s] Sair

"""

def saque(valor):
    global saldo, limite, saques
    if valor > 0:
        if valor <= saldo:
            saques +=1
            if saques <= LIMITE_SAQUE_DIARIO:
                if valor <= limite:
                    saldo -= valor
                    operacoes.append(f'Saque no valor de R$ {valor:.2f}\n')
                    return print("\nSaque efetuado com sucesso\n")
                else:
                    return print("\nLimite do valor de saque atingido\n")
            else:
                return print("\nLimite de saques diarios atingido \n")
        else: 
            return print("\nNão foi possivel efetuar o saque, saldo insuficiente\n")
    else:
        return print("Valor informado é invalido\n")    

def deposito(valor):
    global saldo
    if valor > 0:
        saldo += valor
        operacoes.append(f'Deposito no valor de R$ {valor:.2f}\n')
        return print("\nDeposito efetuado com sucesso\n")
    else:
        return print('Valor informado é invalido')

def extrato():
    global saldo
    texto = '\n'
    for a in operacoes:
        texto += a
    texto += f'__________________\nO saldo Total é: R$ {saldo:.2f}\n'
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
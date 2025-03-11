#atividade 1 - Julynane da Costa Ataides

def criar_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def deposita(conta, valor):
    if valor > 0:
        conta['saldo'] += valor
    else:
        print("Erro: O valor do depósito deve ser positivo.")

def saca(conta, valor):
    if valor > 0:
        if conta['saldo'] >= valor:
            conta['saldo'] -= valor
        else:
            print("Erro: Saldo insuficiente para saque.")
    else:
        print("Erro: O valor do saque deve ser positivo.")

def extrato(conta):
    print("Número: {}\nSaldo: {}".format(conta['numero'], conta['saldo']))


conta = criar_conta("123-4", "João", 120.0, 1000.0)

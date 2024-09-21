print("Seja bem-vindo ao Sistema Bancario")

total = 0
saques = 0
sistema = 1
lista_deposito = []
lista_saque = []

while sistema == 1:
    operacao = int(input("\n[1]Deposito\n[2]Sacar\n[3]Extrato\n[4]Sair\nEscolha: "))

    if operacao == 1:
        valor = float(input("Coloque o valor que deseja depositar: "))
        total += valor
        print("despositado = {}\ntotal = {}".format(valor, total))
        lista_deposito.append(valor)

    elif operacao == 2:
        valor = float(input("Coloque o valor que deseja sacar: "))
        if valor > total:
            print("não é permitido fazer esse saque. valor > total")
        elif saques < 3:
            total -= valor
            saques += 1
            lista_saque.append(valor)
            print("Valor do saque: {}\nValor total: {}".format(valor, total))
            print("Total de Saques: {}/3".format(saques))
        elif valor > 500:
            print("Nao e permitido, seu limite eh 500 por saque")
        else:
            print("estorou o limite de saques")
    
    elif operacao == 3:
        print("\n**********Extrato**************\n")
        print("todos os depositos: {}\ntodos saques: {}\nTotal: {}".format(lista_deposito, lista_saque, total))

    elif operacao == 4:
        sistema = 0

    else:
        print("Escolha uma opcao valida")

print("Obrigado por usar nosso sistema")
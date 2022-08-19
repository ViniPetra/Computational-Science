def PeParaMetro(valor):
    return valor * 0.3048

def MetroParaPe(valor):
    return valor * 3.281

running = True

while(running):
    opc = input("Escolha uma opção:\n1 - Conveter de Pé para Metro\n2 - Converter de Metro para Pé\n")
    valor = input("Digite o valor a ser convertido: ")

    if(opc == "1"):
        res = PeParaMetro(float(valor))
    else:
        res = MetroParaPe(float(valor))

    print(res)

    sair = input("Escolha 1 para sair ou 2 para fazer uma nova conversão: ")

    if(sair == "1"):
        running = False
# Menus da aplicação
## Menu para a primeira jogada
def MenuInicial():
    print("Bem-vind@! Para iniciar a aplicação, por favor crie uma lista:")
    print("1. Criar lista com N números aleatórios")
    print("2. Criar lista com N números escolhidos pelo utilizador")

## Menu geral
def MenuGeral():
    print("Eis as opções desta aplicação:")
    print("1. Criar lista com N números aleatórios")
    print("2. Criar lista com N números escolhidos pelo utilizador")
    print("3. Calcular a soma dos elementos da lista")
    print("4. Calcular a média dos elementos da lista")
    print("5. Calcular o maior elemento da lista")
    print("6. Calcular o menor elemento da lista")
    print("7. Determinar se a lista está ordenada por ordem crescente")
    print("8. Determinar se a lista está ordenada por ordem decrescente")
    print("9. Procurar um elemento na lista")
    print("0. Sair da aplicação")

# Definição das funções do menu
import random

def CriarListaAleatória():
    lista = []
    tamanho = int(input("Introduza o tamanho da lista que pretende criar:"))
    while tamanho > 0:
        num = random.randint(1, 100)
        lista.append(num)
        tamanho = tamanho - 1
    return lista

def CriarListaPersonalizada():
    lista = []
    tamanho = int(input("Introduza o tamanho da lista que pretende criar:"))
    i = 1
    while i <= tamanho:
        num = int(input(f"Introduza o elemento {i}/{tamanho}:"))
        lista.append(num)
        i = i + 1
    return lista

def SomaElem(lista):
    soma = 0
    i = 0
    for i in range(len(lista)):
        soma = soma + lista[i]
        i = i + 1
    return print(f"A soma dos elementos da lista {lista} é {soma}.")

def MédiaLista(lista):
    soma = 0
    i = 0
    for i in range(len(lista)):
        soma = soma + lista[i]
        i = i + 1
    média = soma / len(lista)
    return print(f"A média da lista {lista} é {média}.")

def MaiorElem(lista):
    maior = lista[0]
    for i in range(len(lista)):
        x = lista[i]
        if x > maior:
            maior = x
    return print(f"O maior elemento da lista {lista} é {maior}.")

def MenorElem(lista):
    menor = lista[0]
    for i in range(len(lista)):
        x = lista[i]
        if x < menor:
            menor = x
    return print(f"O maior elemento da lista {lista} é {menor}.")

def EstaOrdCrescente(lista):
    EstaOrdenada = True
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            EstaOrdenada = False
    return print("Sim") if EstaOrdenada else print("Não")

def EstaOrdDecrescente(lista):
    EstaOrdenada = True
    for i in range(len(lista) - 1):
        if lista[i] < lista[i + 1]:
            EstaOrdenada = False
    return print("Sim") if EstaOrdenada else print("Não")

def ProcurarElem(lista):
    elem = float(input("Introduza o elemento que pretende procurar:"))
    HáElem = False
    i = 0
    for i in range (len(lista)):
        if lista[i] == elem:
            localização = i
            HáElem = True
    return print(f"{localização}") if HáElem else print("-1")

# Programa Principal
MenuInicial()
lista_armazenada = []
opção1 = int(input("Introduza a opção desejada:"))
if opção1 == 1:
    lista_armazenada = CriarListaAleatória()
    print(lista_armazenada)
elif opção1 == 2:
    lista_armazenada = CriarListaPersonalizada()
    print(lista_armazenada)

MenuGeral()
opção = int(input("Introduza a opção desejada:"))
while opção != 0:
    if opção == 1:
        lista_armazenada = CriarListaAleatória()
        print(lista_armazenada)
        MenuGeral()
        opção = int(input("Introduza a opção desejada:"))
    elif opção == 2:
        lista_armazenada = CriarListaPersonalizada()
        print(lista_armazenada)
        MenuGeral()
        opção = int(input("Introduza a opção desejada:"))
    elif opção == 3:
        SomaElem(lista_armazenada)
        MenuGeral()
        opção = int(input("Introduza a opção desejada:"))
    elif opção == 4:
        MédiaLista(lista_armazenada)
        MenuGeral()
        opção = int(input("Introduza a opção desejada:"))
    elif opção == 5:
        MaiorElem(lista_armazenada)
        MenuGeral()
        opção = int(input("Introduza a opção desejada:"))
    elif opção == 6:
        MenorElem(lista_armazenada)
        MenuGeral()
        opção = int(input("Introduza a opção desejada:"))
    elif opção == 7:
        EstaOrdCrescente(lista_armazenada)
        MenuGeral()
        opção = int(input("Introduza a opção desejada:"))
    elif opção == 8:
        EstaOrdDecrescente(lista_armazenada)
        MenuGeral()
        opção = int(input("Introduza a opção desejada:"))
    elif opção == 9:
        ProcurarElem(lista_armazenada)
        MenuGeral()
        opção = int(input("Introduza a opção desejada:"))
print(f"A lista atualmente armazenada é {lista_armazenada}.")

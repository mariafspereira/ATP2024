# Menu principal
## Seleção da opção pretendida
def print1():
    print("\n===== Menu ===== \n (1) Temperatura média \n(2) Guardar tabela num ficheiro \n(3) Carregar tabela de um ficheiro \n(4) Temperatura mínima mais baixa \n(5) Valor mais alto de percipitação \n(6) Número de dias com a percipitação superior a "x" \n(7) Maior número de dias consecutivos com percipitação abaixo de "x" \n(8) Gráfico de temperatura máxima e mínima \n(9) Gráfico de pluviosidade \n(0) Sair da aplicação")
    opção = int(input("\nInsira o número da opção desejada: "))

def menu():
    tabmeteo = []
    print("\n===== Menu ===== \n (1) Temperatura média \n(2) Guardar tabela num ficheiro \n(3) Carregar tabela de um ficheiro \n(4) Temperatura mínima mais baixa \n(5) Valor mais alto de percipitação \n(6) Número de dias com a percipitação superior a "x" \n(7) Maior número de dias consecutivos com percipitação abaixo de "x" \n(8) Gráfico de temperatura máxima e mínima \n(9) Gráfico de pluviosidade \n(0) Sair da aplicação")
    opção = int(input("\nInsira o número da opção desejada: "))
    while opção != 0:
        if opção == 1:
            medias(tabmeteo)
        elif opção == 2:
            guardaTabMeteo(tabmeteo, "C:\\Ambiente de trabalho\\Arquivo\\Escola\\LEB\\2º Ano\\1º Semestre\\Programação\\GitHub\\ATP2024\\TP7\\meteorologia.txt")
        elif opção == 3:
            tabmeteo = carregaTabMeteo("C:\\Ambiente de trabalho\\Arquivo\\Escola\\LEB\\2º Ano\\1º Semestre\\Programação\\GitHub\\ATP2024\\TP7\\meteorologia.txt")
            print(tabmeteo)
        elif opção == 4:
            minMin(tabmeteo)
        elif opção == 5:
            maxChuva(tabmeteo)
        elif opção == 6:
            p = float(input("Que limite deseja? "))
            diasChuvosos(tabmeteo, p)
        elif opção == 7:
            p = float(input("Que limite deseja? "))
            maxPeriodoCalor(tabmeteo, p)
        elif opção == 8:
            grafTabMeteoTemp(tabmeteo)
        elif opção == 9:
            grafTabMeteoPulv(tabmeteo)
        else:
            print("Insira um modo válido!")
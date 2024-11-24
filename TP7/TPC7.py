# Menu principal
def menu():
    tabmeteo = []
    v = True 
    while v == True:
        print("""\n===== Menu =====
(1): Temperatura média;
(2): Guardar tabela num ficheiro;
(3): Carregar tabela de um ficheiro;
(4): Temperatura mínima mais baixa;
(5): Valor mais alto de percipitação;
(6): Número de dias com a percipitação superior a "x";
(7): Maior número de dias consecutivos com percipitação abaixo de "x";
(8): Gráfico de temperatura máxima e mínima;
(9): Gráfico de pluviosidade;
(0): Sair da aplicação""") 
        modo = int(input("Que modo deseja? "))

        if modo == 1:
            medias(tabmeteo)
        elif modo == 2:
            guardaTabMeteo(tabmeteo, "C:\\Users\\ze05p\\OneDrive\\Documentos\\Licenciatura em Engenharia Biomédica\\2º Ano\\1º Semestre\\Algoritmos e Técnicas de Programação\\Os meus Noteebooks\\TPC7\\meteorologia.txt")
        elif modo == 3:
            tabmeteo = carregaTabMeteo("C:\\Users\\ze05p\\OneDrive\\Documentos\\Licenciatura em Engenharia Biomédica\\2º Ano\\1º Semestre\\Algoritmos e Técnicas de Programação\\Os meus Noteebooks\\TPC7\\meteorologia.txt")
            print(tabmeteo)
        elif modo == 4:
            minMin(tabmeteo)
        elif modo == 5:
            maxChuva(tabmeteo)
        elif modo == 6:
            p = float(input("Que limite deseja? "))
            diasChuvosos(tabmeteo, p)
        elif modo == 7:
            p = float(input("Que limite deseja? "))
            maxPeriodoCalor(tabmeteo, p)
        elif modo == 8:
            grafTabMeteoTemp(tabmeteo)
        elif modo == 9:
            grafTabMeteoPulv(tabmeteo)
        elif modo == 0: 
            print("Programa Encerrado.")
            v = False
        else:
            print("Insira um modo válido!")
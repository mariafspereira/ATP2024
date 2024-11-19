#Definir Funções

## (1) Inserir Salas
cinema = []
def inserir_salas(cinema):
    s = int(input(f"\nQuantas salas quer adicionar? Atualmente há {len(cinema)} salas."))
    while s > 0:
        sala = []  #sala=[NLugares, Vendidos, Filme, LInterditos]
        
        print("\n=====Nova sala=====")
        NLugares = int(input("Introduza o número de lugares da nova sala: "))
        lugares = list(range(1, NLugares + 1))
        sala.append(lugares)

        vendidos = 0
        sala.append(vendidos)

        filme = str(input("Introduza o nome do filme: "))
        sala.append(filme)
        
        LugaresInterditos = 0
        sala.append(LugaresInterditos)
        
        s = s - 1
        cinema.append(sala)
    return cinema

## (2) Listar Filmes
def listar_filmes(cinema):   #sala=[NLugares, Vendidos, Filme, LInterditos]
    if len(cinema) == 0:
        print("\nNão há salas!")
    else:
        ContadorSala = 1
        for sala in cinema:
            print(f"Sala {ContadorSala} \nFilme '{sala[2]}'")
            ContadorSala = ContadorSala + 1

## (3) Disponibilidade de Lugar
def listar_disponibilidade(cinema):   #sala=[NLugares, Vendidos, Filme, LInterditos]
    if len(cinema) == 0:
        print("\nNão há salas!")
    else:
        ContadorSala = 1
        for sala in cinema:
            print(f"\nSala {ContadorSala} \nFilme: '{sala[2]}' \nLugares: {len(sala[0])}")
            ContadorLugar = 1
            for lugar in sala[0]: 
                    print(lugar, end=' ') 
                    ContadorLugar = ContadorLugar + 1
            print(f"\n *Bilhetes vendidos: {sala[1]} \n *Lugares disponíveis: {len(sala[0]) - sala[1] - sala[3]} \n *Lugares interditos: {sala[3]}")
            ContadorSala = ContadorSala + 1

## (4) Editar Salas
def editar_salas(cinema):   #sala=[NLugares, Vendidos, Filme, LInterditos]
    print("\n(1) Mudar nome do Filme \n(2) Remover Filme \n(3) Interditar Lugares \n(0) Voltar ao Menu ")
    opção1 = int(input("Insira o número da opção desejada: "))
    while opção1 != 0:
        if opção1 == 1:
            SalaSelecionada = int(input(f"\nEscolha o número da sala: 1 a {len(cinema)}): ")) - 1
            if 0 <= SalaSelecionada < len(cinema):
                cinema[SalaSelecionada][2] = str(input("Introduza o novo nome do filme: "))
                print(f"Alteração realizada com sucesso!")
            else:
                print("Número da sala inválido.")
        elif opção1 == 2:
            SalaSelecionada = int(input(f"\nEscolha o número da sala: 1 a {len(cinema)}): ")) - 1
            if 0 <= SalaSelecionada < len(cinema):
                cinema[SalaSelecionada][2] = "Sem Filme"
                print(f"Alteração realizada com sucesso!")
            else:
               print("Número da sala inválido.") 
        elif opção1 == 3:
            SalaSelecionada = int(input(f"\nEscolha o número da sala: 1 a {len(cinema)}): ")) - 1
            if 0 <= SalaSelecionada < len(cinema):
                lugar = int(input(("Introduza o número do lugar que pretende interditar: ")))
                if lugar in cinema[SalaSelecionada][0]:
                    for número in cinema[SalaSelecionada][0]:
                        if número == lugar:  
                            cinema[SalaSelecionada][0][lugar - 1] = "I"   #Marcação do Lugar como 'Interdito'
                            cinema[SalaSelecionada][3] = cinema[SalaSelecionada][3] + 1
                            print("Alteração realizada com sucesso!")
                else:
                    print("O lugar introduzido não existe na sala selecionada.")      
            else:
                print("Número da sala inválido.")  
        else:
            print("Opção desconhecida.")

## (5) Vender Bilhetes
def vender_bilhetes(cinema):   #sala=[NLugares, Vendidos, Filme, LInterditos]
    SalaSelecionada = int(input(f"\nEscolha o número da sala: 1 a {len(cinema)}): ")) - 1
    if cinema[SalaSelecionada][2] != "Sem Filme":
        NBilhetes = int(input("Introduza o número de bilhetes que pretende comprar: "))
        if 0 <= SalaSelecionada < len(cinema):
            sala = cinema[SalaSelecionada]
            if len(sala[0]) - sala[1] >= NBilhetes:
                sala[1] = sala[1] + NBilhetes  
            else:
                print(f"Na sala selecionada há apenas {len(sala[0]) - sala[1]} lugares disponíveis.")
        else:
            print("Número da sala inválido.")

        for lugar in cinema[SalaSelecionada][0]: 
                    print(lugar, end=' ') 

        i = 1
        while i < NBilhetes:
            lugar = int(input((f"Escolha o lugar do bilhete {i}/{NBilhetes}: ")))
            if lugar in cinema[SalaSelecionada][0]:
                for número in cinema[SalaSelecionada][0]:
                    if número == lugar:  
                        cinema[SalaSelecionada][0][lugar - 1] = "R"   #Marcação do Lugar como 'Reservado'
                        i = i + 1
            else:
                print("O lugar selecionado não está disponível.")
        cinema[SalaSelecionada][1] = cinema[SalaSelecionada][1] + NBilhetes
    else:
        print("A sala selecionada não tem nenhum filme.")

# Menu Principal
def menu():
    cinema = []
    print("\n===== Menu =====\n(1) Inserir Salas \n(2) Listar Filmes \n(3) Disponibilidade de Lugar \n(4) Editar Salas \n(5) Vender Bilhete\n (0) Sair do Programa") 
    opção = int(input("Insira o número da opção desejada: "))
    while opção != 0:
        if opção == 1:
            inserir_salas(cinema)
        elif opção == 2:
            if len(cinema) == 0:
                print("\nNão há salas!")
                opção = int(input("\nInsira o número da opção desejada: "))
            else:
                listar_filmes(cinema)
        elif opção == 3:
            if len(cinema) == 0:
                print("\nNão há salas!")
                opção = int(input("\nInsira o número da opção desejada: "))
            else:
                listar_disponibilidade(cinema)
        elif opção == 4:
            if len(cinema) == 0:
                print("\nNão há salas!")
                opção = int(input("\nInsira o número da opção desejada: "))
            else:
                editar_salas(cinema)
        elif opção == 5:
            if len(cinema) == 0:
                print("\nNão há salas!")
                opção = int(input("\nInsira o número da opção desejada: "))
            else:
                vender_bilhetes(cinema)
        elif opção == 0: 
            print("\nPrograma Encerrado.")
        else:
            print("\nOpção desconhecida.")
            opção = int(input("\nInsira o número da opção desejada: "))

menu()
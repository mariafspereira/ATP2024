# Menu Principal
## Seleção da opção pretendida
def print1():
    print("\n===== Menu ===== \n(1) Criar uma turma \n(2) Inserir um aluno na turma \n(3) Listar as turma \n(4) Consultar um aluno por \n(5) Guardar a turma em ficheiro \n(6) Carregar uma turma dum ficheiro \n(0) Sair da aplicação") 
    opção = int(input("\nInsira o número da opção desejada: "))

def menu():
    escola = []
    print("\n===== Menu ===== \n(1) Criar uma turma \n(2) Inserir um aluno na turma \n(3) Listar as turma \n(4) Consultar um aluno por ID \n(5) Guardar a turma em ficheiro \n(6) Carregar uma turma dum ficheiro \n(0) Sair da aplicação") 
    opção = int(input("\nInsira o número da opção desejada: "))
    while opção != 0:
        if opção == 1:
            cria_turma(escola)
            print1()
        elif opção == 2:
            inserir_aluno(escola)
            print()
        elif opção == 3:
            listar_turmas(escola)
            print1()
        elif opção == 4:
            consultar_aluno(escola)
            print1()
        elif opção == 5:
            guardar(escola)
            print1()
        elif opção == 6:
            escola = carregar("escola.txt")
            print1()
        else:
            print("Opção desconhecida.")

# Definir Funções
## (1) Criar uma Turma
def cria_turma(escola):
    escola.append([])
    print(f"Alteração realizada com sucesso! \nAtualmente há {len(escola)} turmas.")
    opção1 = str. lower(input("Deseja adicionar alunos à turma criada? (s/n)"))
    if opção1 == 's':
        inserir_aluno(escola)
    else:
        print("Alteração realizada com sucesso!")

## (2) Inserir um aluno na turma 
def inserir_aluno(escola):   #Aluno = (nome, ID, [notas])
        listar_turmas(escola)
        turma = int(input(f"\nInsira o número da turma a que pretende adicionar o aluno: ")) - 1
        if (turma + 1) > len(escola):
            print("Número da turma inválido.")
        else:
            NomeAluno = (str(input("Insira o nome do aluno: ")))
            IDAlunos = (str(input("Insira o ID do aluno: ")))
            Notas = []
            NotaTPC = float(input("Insira a nota do TPC: "))
            Notas.append(NotaTPC)
            NotaProjeto = float(input("Insira a nota do Projeto: "))
            Notas.append(NotaProjeto)
            NotaTeste = float(input("Insira a nota do Teste: "))
            Notas.append(NotaTeste)
            aluno = (NomeAluno, IDAlunos, Notas)
            escola[turma].append(aluno)

## (3) Listar as turma
def listar_turmas(escola):   #Aluno = (nome, ID, [notas])
    ContadorTurma = 1
    for turma in escola:
        print(f"\nTurma {ContadorTurma}:")
        for aluno in turma:
            print(f" *{aluno[0]}, ID: {aluno[1]} | Nota TPC: {aluno[2][0]}; Nota Projeto: {aluno[2][1]}; Nota Teste: {aluno[2][2]}")
        ContadorTurma = ContadorTurma + 1

## (4) Consultar um aluno por id    
def consultar_aluno(escola):   #Aluno = (nome, ID, [notas])
        NTurma = 1
        aluno_encontrado = False
        ID = input("Insira o ID do aluno que pretende procurar: ")
        for turma in escola:
            for aluno in turma:
                if aluno[1] == ID:
                    print(f"\nO aluno com o ID {ID} está inscrito na turma {NTurma}: {aluno[0]}, ID: {aluno[1]} | Nota TPC: {aluno[2][0]}; Nota Projeto: {aluno[2][1]}; Nota Teste: {aluno[2][2]}")
                    aluno_encontrado = True
            NTurma = NTurma + 1
        if not aluno_encontrado:
            print(f"\nO aluno com ID {ID} não está inscrito em nenhuma turma.")

## (5) Guardar a turma em ficheiro  
def guardar(escola):
    file = open("escola.txt", "w")
    file.write(escrever_turma(escola))
    file.close()
    print("Alteração realizada com sucesso!")
 
def escrever_turma(escola):
    listar_turmas(escola)
    opção2 = int(input("Introduza o número da turma que pretende guardar em ficheiro: ")) - 1
    TurmaEscolhida = escola[opção2]
    for aluno in TurmaEscolhida:
        print(str(f"{aluno[0]}; ID: {aluno[1]}; Nota TPC: {aluno[2][0]}; Nota Projeto: {aluno[2][1]}; Nota Teste: {aluno[2][2]}"))

## (6) Carregar uma turma dum ficheiro   
def carregar(NomeFicheiro):
    turma = []
    with open(NomeFicheiro, "r") as file:
        for linha in file:
            linha = linha.strip()
            if linha != "":
                campos = linha.split(",")
                if len(campos) >= 5:
                    nome = str(campos[0])
                    ID = str(campos[1])
                    notas = [float(campos[2]), float(campos[3]), float(campos[4])]
                    turma.append((nome, ID, notas))
            escola = escola.append(turma)
    print("Alteração realizada com sucesso!")
    return escola

menu()
# Jogo dos fósforos
def menu_1():
    print("Bem-vindo ao Jogo dos fósforos!")
    print("As regras são as seguintes: O jogo começa com 21 fósforos e, em cada jogada, cada jogador tema escolha de retirar entre 1 a 4 fósforos. Os jogadores jogam alternadamente e o objetivo é deixar sempre fósforos em jogo. Quem tirar o último fósforo... perde!")

def menu_2():
    print("Eis os possíveis modos de jogo:")
    print("1. O jogador joga em primeiro lugar")
    print("2. O computador joga em primeiro lugar")
    print("0. Sair")

## Modo 1: Vertente em que o jogador joga em primeiro lugar
def modo_1():
    fósforos = 21
    print("Há 21 fósforos em jogo.")
    while fósforos > 1:
        jogada1 = int(input("Escolhe o número de fósforo que queres tirar:"))
        fósforos = fósforos - jogada1
        print(f"Retiraste {jogada1} fósforos. Há agora {fósforos} em jogo.")
        jogada2 = 5 - jogada1
        fósforos = fósforos - jogada2
        print(f"Quero tirar {jogada2} fósforos. Assim, sobram {fósforos} em jogo.")
    print("Oops... É a tua vez de jogar e só há 1 fósforo na mesa...Perdeste!")

## Modo 2: Vertente em que o computador joga em primeiro lugar
def modo_2():
    jogada = 0
    fósforos = 21
    print("Há 21 fósforos em jogo.")
    while fósforos > 1:
        from random import randint
        jogada1 = randint(1, 4)
        jogada = jogada + 1
        fósforos = fósforos - jogada1
        print(f"Quero tirar {jogada1} fósforos. Há agora {fósforos} em jogo.")
        jogada2 = int(input("Escolhe o número de fósforos de queres tirar:"))
        jogada = jogada + 1
        while jogada2 < 1 or jogada2 > 4:
            print("Erro! Deve escolher entre 1 e 4 fósforos.")
            jogada2 = int(input("Escolhe o número de fósforos de queres tirar:"))
        fósforos = fósforos - jogada2
        print(f"Retiraste {jogada2} fósforos. Assim, sobram {fósforos} em jogo.")

        if jogada1 + jogada2 == 5:
            jogada1 = randint(1, 4)
            jogada = jogada + 1
            fósforos = fósforos - jogada1
            print(f"Quero tirar {jogada1} fósforos. Há agora {fósforos} em jogo.")
            jogada2 = int(input("Escolhe o número de fósforos de queres tirar:"))
            jogada = jogada + 1
            while jogada2 < 1 or jogada2 > 4:
                print("Erro! Deve escolher entre 1 e 4 fósforos.")
                jogada2 = int(input("Escolhe o número de fósforos de queres tirar:"))
            fósforos = fósforos - jogada2
            print(f"Retiraste {jogada2} fósforos. Assim, sobram {fósforos} em jogo.")

        elif jogada1 + jogada2 != 5:
            jogada1 = (fósforos - 1) % 5
            jogada = jogada + 1
            fósforos = fósforos - jogada1
            print(f"Quero tirar {jogada1} fósforos. Há agora {fósforos} em jogo.")
            jogada2 = int(input("Escolhe o número de fósforos de queres tirar: "))
            jogada = jogada + 1
            while jogada2 < 1 or jogada2 > 4:
                print("Erro! Deve escolher entre 1 e 4 fósforos.")
                jogada2 = int(input("Escolhe o número de fósforos de queres tirar: "))
            fósforos = fósforos - jogada2
            print(f"Retiraste {jogada2} fósforos. Assim, sobram {fósforos} em jogo.")

    if fósforos == 1 and jogada % 2 == 0:
        print("Oops... É a minha vez de jogar e só há 1 fósforo na mesa... Ganhaste!")
    else:
        print("Já não há fósforos na mesa... Perdeste!")

## Programa principal
menu_1()
menu_2()

opção = int(input("Introduza a opção desejada:"))
while opção != 0:
    if opção == 1:
        modo_1()
        menu_2()
    elif opção == 2:
        modo_2()
        menu_2()
print("Até à próxima!")
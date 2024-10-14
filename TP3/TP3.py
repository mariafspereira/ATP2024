# Jogo dos fósforos
## Menu do jogo
def menu():
    print("Bem-vindo ao Jogo dos Fósforos!")
    print("As regras são: Inicialmente há 21 fósforos na mesa. Cada jogador retira alternadamente da mesa entre 1 a 4 fósforos. O jogador a retirar o último fósforo da mesa... perde!")
    print("Existem dois modos de jogo:")
    print("a) O jogador começa a jogar")
    print("b) O computador começa a jogar")

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
    fósforos = 21
    print("Há 21 fósforos em jogo.")
    from random import randint
    jogada1 = randint(1, min(4, fósforos))
    fósforos = fósforos - jogada1
    print(f"Quero tirar {jogada1} fósforos. Há agora {fósforos} em jogo.")
    jogada2 = int(input("Escolhe o número de fósforos de queres tirar:"))
    while jogada2 < 1 or jogada2 > 4:
        print("Erro! Deve escolher entre 1 e 4 fósforos.")
        jogada2 = int(input("Escolhe o número de fósforos de queres tirar:"))
    fósforos = fósforos - jogada2
    print(f"Retiraste {jogada2} fósforos. Assim, sobram {fósforos} em jogo.")
    ftirados = jogada1 + jogada2

    while fósforos > 0:
        if ftirados == 5:
            jogada1 = randint(1, min(4, fósforos))
            fósforos = fósforos - jogada1
            print(f"Quero tirar {jogada1} fósforos. Há agora {fósforos} em jogo.")
            jogada2 = int(input("Escolhe o número de fósforos de queres tirar:"))
            while jogada2 < 1 or jogada2 > 4:
                print("Erro! Deve escolher entre 1 e 4 fósforos.")
                jogada2 = int(input("Escolhe o número de fósforos de queres tirar:"))
            fósforos = fósforos - jogada2
            print(f"Retiraste {jogada2} fósforos. Assim, sobram {fósforos} em jogo.")
            ftirados = jogada1 + jogada2
            if fósforos == 1:
                print("Retiro 1 fósforo... Ganhaste!")
                fósforos = 0

        elif ftirados > 5:
            jogada1 = 10 - ftirados
            fósforos = fósforos - jogada1
            print(f"Quero tirar {jogada1} fósforos. Há agora {fósforos} em jogo.")
            jogada2 = int(input("Escolhe o número de fósforos de queres tirar: "))
            while jogada2 < 1 or jogada2 > 4:
                print("Erro! Deve escolher entre 1 e 4 fósforos.")
                jogada2 = int(input("Escolhe o número de fósforos de queres tirar: "))
            fósforos = fósforos - jogada2
            print(f"Retiraste {jogada2} fósforos. Assim, sobram {fósforos} em jogo.")
            ftirados = jogada2
            if fósforos == 0:
                print("Já não há fósforos na mesa... Perdeste!")
       
        elif ftirados <= 5:
            jogada1 = 5 - ftirados
            fósforos = fósforos - jogada1
            print(f"Quero tirar {jogada1} fósforos. Há agora {fósforos} em jogo.")
            jogada2 = int(input("Escolhe o número de fósforos de queres tirar: "))
            while jogada2 < 1 or jogada2 > 4:
                print("Erro! Deve escolher entre 1 e 4 fósforos.")
                jogada2 = int(input("Escolhe o número de fósforos de queres tirar: "))
            fósforos = fósforos - jogada2
            print(f"Retiraste {jogada2} fósforos. Assim, sobram {fósforos} em jogo.")
            ftirados = jogada2
            if fósforos == 0:
                print("Já não há fósforos na mesa... Perdeste!")

##Programa principal
menu()
modo = input("Escolha uma opção:")
if modo == "a":
    modo_1()
elif modo == "b":
    modo_2()
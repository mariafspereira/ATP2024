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
    while fósforos > 1:
        from random import randrange
        jogada_pc = randrange(1, 5)
        fósforos = fósforos - jogada_pc
        print(f"Quero tirar {jogada_pc} fósforos. Há agora {fósforos} em jogo.")
        jogada_jog = int(input("Escolhe o número de fósforos de queres tirar:"))
        fósforos = fósforos - jogada_jog
        print(f"Retiraste {jogada_jog} fósforos. Assim, sobram {fósforos} em jogo.")

    if fósforos == 1:
        print("Boa!! É a minha vez de jogar e só há 1 fósforo na mesa... Ganhaste!")

    else:
        if fósforos <= 5:
            jogada_pc = fósforos - 1
        else: #fósforos >= 5
            if fósforos % 5 == 1:
                from random import randrange
                jogada_pc = randrange(1, 5)
            else: #fósforos % 5 != 1
                jogada_pc = (fósforos % 5) - (jogada_jog)
        fósforos = fósforos - jogada_pc
            
        if fósforos == 1:
            print("Oops... É a tua vez de jogar e só há 1 fósforo na mesa... Perdeste!")

##Programa principal
menu()
modo = input("Escolha uma opção:")
if modo == "a":
    modo_1()
elif modo == "b":
    modo_2()
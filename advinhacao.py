import random


def jogar():
    print("*******************************")
    print("Bem vindo no jogo de Advinhação")
    print("*******************************")

    numero_secreto = random.randrange(1, 100) + 1
    total_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if nivel == 1:
        total_tentativas = 20
    elif nivel == 2:
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas):

        print("Tentativa {} de {}".format(rodada, total_tentativas))

        chute_str = input("Digite o seu numero: ")

        print("Você digitou ", chute_str)

        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100")
            continue

        if numero_secreto == chute:
            print("Você acertou! Fechou o jogo com {} pontos!".format(pontos))
            break

        else:
            if chute < numero_secreto:
                print("Você errou! O número secreto é maior que " + chute_str)
            elif chute > numero_secreto:
                print("Você errou! O número secreto é menor que " + chute_str)
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do Jogo!!")


if __name__ == "__main__":
    jogar()

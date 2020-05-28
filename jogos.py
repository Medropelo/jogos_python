import forca
import advinhacao


def escolhe_jogo():
    print("*******************************")
    print("****** Escolha seu Jogo! ******")
    print("*******************************")

    print("(1) Forca (2) Advinhação")

    jogo = int(input("Qual Jogo?"))

    if jogo == 1:
        print("Abrindo Jogo da Forca...")
        forca.jogar()
    elif jogo == 2:
        print("Abrindo Jodo da Advinhação...")
        advinhacao.jogar()


if __name__ == "__main__":
    escolhe_jogo()

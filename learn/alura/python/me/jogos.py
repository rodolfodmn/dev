import forca
import adivinha


def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca (2) Adivinha")

    jogo = int(input("qual jogo?"))

    if(jogo == 1):
        print("jogando forca")
        forca.jogar()
    elif (jogo == 2):
        print("jogando adivinha")
        adivinha.jogar()

if __name__ == "__main__":
    escolhe_jogo()

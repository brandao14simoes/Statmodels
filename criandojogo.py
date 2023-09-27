import random
from os import system, name

def limpa_tela():

    if name == 'int':
        _ = system('clear')
    else:
        _ = system('cls')
        
def game():

    limpa_tela()
    print("\nJogo da Forca!")
    print("Adivinhe a palavra abaixo:\n")

    #Lista das palavras 
    palavras = ['prego', 'martelo', 'porca', 'parafuso']

    palavra = random.choice(palavras)

    lista_letras_palavras = [letra for letra in palavra]

    tabuleiro = ["_"] * len (palavra)

    chances = 10

    letras_tentativas = []

    while chances > 0:
        #Exibe o Tabuleiro
        print(" ".join(letras_descobertas))
        print("\n Chances restantes:", chances)
        print("Letras erradas:", " ".join(letras_erradas))

        tentativa = input("\n Digite uma letra: ").lower()

        if tentativa in letras_tentativas:
            print("Você já tentou essa letra. Escolha outra!")
            continue

            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index +=1

            if "_" not in letras_descobertas:
                print("\n Você venceu, palavra é:", palavra)
            break

        else:
            print("Essa letra não está na palavra")
            chances -=1
            letras_erradas.append(tentativa)
    
    if "_" in letras_descobertas:
        print("\nVocê perdeu, palavra era:", palavra)

if __name__ == "__main__":
    game()
    print("\nParabnes. Você está indo bem !")
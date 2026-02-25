from random import randint
from time import sleep
import os



def clean_console():
    """Cleans the console depending on your operative system"""
    os.system('cls' if os.name == 'nt' else 'clear')

def hanged(fails):
    # "  +---+",
    # "  |   |",
    # "  O   |",
    # " /|\  |",
    # " / \  |",
    # "      |",
    # "======="
    hanged = ["  +---+",
              "  |   |",
              "      |",
              "      |",
              "      |",
              "      |",
              "======="]
    
    if fails >= 1:
        hanged[2] = "  O   |"
    if fails >= 2:
        hanged[3] = "  |   |"
    if fails >= 3:
        hanged[3] = " /|   |"
    if fails >= 4:
        hanged[3] = " /|\  |"
    if fails >= 5:
        hanged[4] = " /    |"
    if fails >= 6:
        hanged[4] = " / \  |"

    return hanged

def main():
    clean_console()
    d = open("./diccionario.txt", "r")
    words = d.read()
    d.close()

    # ----- Seleccion de la palabra aleatoria -----
    random_index = randint(0, len(words.split("\n")) - 1)
    word = words.split("\n")[random_index] # Seleccionamos la palabra aleatoria
    len_word = len(word) 
    unknown_word = ["_"] * len_word # Crear la palabra con "_"
    fails = 0
    used_letters = [] # Lista de letras usadas

    # Mientras no se adivine la palabra
    while unknown_word != list(word) and fails < 6:
        print("--- AHORCADO ---")

        # ----- Dibujo del ahorcado -----
        hanged_print = hanged(fails)
        for line in hanged_print:
            print(line)

        # ----- Muestra la palabra a adivinar -----
        for i in range(0, len_word):
            print(unknown_word[i], end=" ")
        print()

        print("[ ", end="")
        for used_letter in used_letters:
            print(used_letter, end=", ")
        print("]")

        # ----- Comprobación de la letra -----
        letter = input("Introduce una letra: ").strip().lower()

        if letter in word:
            for i in range(0, len_word):
                if word[i] == letter:
                    unknown_word[i] = letter

        elif letter in used_letters:
            print(f"La letra {letter} ya ha sido usada")

        elif len(letter) != 1 or not letter.isalpha():
            print("Introduce una letra válida")

        else:
            used_letters.append(letter)
            fails += 1

            print(f"La letra {letter} no está en la palabra")
        
        sleep(1)
        clean_console()

    # ----- Menasaje final -----
    print("--- AHORCADO ---")
    if fails == 6:
        print("Has perdido! La plabra era:", word)
    else:
        print("Felicidades! Has ganado! La palabra era:", word)


if __name__ == "__main__":
    main()

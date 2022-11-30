import random
from words import words
from hangman_visual import lives_visual_dict
import string


def get_valid_word(words):
    word = random.choice(words)  # Elije algo aleatoriamente de la lista
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  #Letras en la palabra
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # Lo que el usuario ha adivinado

    lives = 7

    # Obteniendo la entrada del usuario
    while len(word_letters) > 0 and lives > 0:
        # Letras usadas
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('Tu tienes', lives, 'vidas que gastaste y has usado estas letras: ', ' '.join(used_letters))

        # cual es la palabra actual (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Palabra actual: ', ' '.join(word_list))

        user_letter = input('Adivina una letra: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # Resta una vida si se equivoca
                print('\nTu letra,', user_letter, 'no esta en la palabra.')

        elif user_letter in used_letters:
            print('\nYa has usado esa letra. Adivina otra letra.')

        else:
            print('\nEsa no es una letra valida.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print('Moriste, lo siento, la palabra era', word)
    else:
        print('¡HURRA! Adivinaste la letra', word, '!!')


if __name__ == '__main__':
    hangman()

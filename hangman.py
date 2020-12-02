import os
import time

HANGMAN = [
    """
           ___
              |
              |
              |
              |
             ===""",
    """
           ___
           |  |
              |
              |
              |
             ===""",
    """
           ___
           |  |
           O  |
              |
              |
             ===""",
    """
           ___
           |  |
           O  |
           |  |
              |
             ===""",
    """
           ___
           |  |
           O  |
           |  |
            \ |
             ===""",
    """
           ___
           |  |
           O  |
           |  |
          / \ |
             ===""",
    """
           ___
           |  |
           O  |
           |\ |
          / \ |
             ===""",
    """
           ___
           |  |
           O  |
          /|\ |
          / \ |
             ==="""]


# Очитска экрана. Из IDLE не работает. Только терминал!
def clear():
    """
    Clears the terminal screen and scroll back to present
    the user with a nice clean, new screen. Useful for managing
    menu screens in terminal applications.
    """
    os.system('cls' if os.name == 'nt' else 'echo -e \\\\033c')


print('A bunch of garbage so we can garble up the screen...')
clear()


# Same effect, less characters...


def clear():
    """
    Clears the terminal screen and scroll back to present
    the user with a nice clean, new screen. Useful for managing
    menu screens in terminal applications.
    """
    os.system('cls||echo -e \\\\033c')


def game():
    print('В И С Е Л И Ц А\n\n')
    word = input('Загадай слово и нажми Enter: ').lower()
    clear()
    print('Слово загадано. Можем начинать...')
    time.sleep(2)
    mistake_letters = []
    good_letter = []
    count_good_letter = 0
    key = True
    while key:
        clear()
        if len(mistake_letters) == len(HANGMAN) - 1:
            print(HANGMAN[-1])
            print('Вы проиграли! Загаданное слово было: ' + word)
            break
        else:
            print(HANGMAN[len(mistake_letters)])
        print('Ошибочные буквы: ', mistake_letters)
        print('Загаданное слово: ', end='')
        for let in word:
            if let in good_letter:
                print(let + ' ', end='')
            else:
                print('_ ', end='')
        print()
        letter = input('Введите букву: ').lower()
        if len(letter) == 0 or len(letter) > 1:
            print('Необходимо ввести только одну букву! Для продолжения нажмите Enter', end=' ')
            input()
            continue
        if letter in word:
            if letter in good_letter:
                print('Такую букву уже называли! Для продолжения нажмите Enter', end=' ')
                input()
                continue
            good_letter.append(letter)
            count_good_letter += word.count(letter)
            if count_good_letter == len(word):
                print('Ура! Вы победили! Загаданное слово действительно: ' + word)
                key = False

        else:
            if letter in mistake_letters:
                print('Такую букву уже называли! Для продолжения нажмите Enter', end=' ')
                input()
                continue
            mistake_letters.append(letter)


key = True
while key:
    game()
    if input('\n\nХотите сыграть еще раз? Да/Нет    ') not in 'Да Д ДА да д Yes YES Y yes y'.split():
        print('Всего доброго.')
        key = False


# cold-hot
import random
import os

MAX_GUESS = 10
NUM_DIGITS = 3


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


def say_rules():
    return print(f"Я загадаю {NUM_DIGITS}-х значное чило, которое вы должны отгадать.\n"
                 "Я дам несколько подсказок...\n\n"
                 "Когда я говорю:      Это означает:\n\n"
                 "Холодно              Ни одна цифра не отгадана\n"
                 "Тепло                Одна цифра отгадана, но не отгадана позиция\n"
                 "Горячо               Одна цифра и ее позиция отгаданы\n\n"
                 "Помните: цифры в числе могут повторяться!\n"
                 "Итак, я загадал число.\n\n"
                 f"У Вас есть {MAX_GUESS} попыток, чтобы его отгадать")


def get_secret_number():
    return str(random.randint(10 ** (NUM_DIGITS - 1), (10 ** NUM_DIGITS) - 1))


def count_attempts(num):
    count = 0
    while count <= num:
        count += 1
        yield count


def make_player_number(num):
    global NUM_DIGITS
    print(f'Попытка №{next(num)}')
    while True:
        try:
            value = input()
            if len(value) == NUM_DIGITS and value.isdigit():
                return value
            print(f'Вводить необходимо {NUM_DIGITS}-значное число! Попробуйте еще раз:', end=' ')
            continue
        except ValueError:
            print(f'Необходимо ввесли {NUM_DIGITS}-значное число! Попробуйте еще раз:', end=' ')


def is_number(num_comp: str, num_pl: str):
    res = []
    for i in range(len(num_pl)):
        if num_comp[i] == num_pl[i]:
            res.append('Горячо')
        elif num_comp[i] in num_pl:
            res.append('Тепло')
    if len(res) == 0:
        res.append('Холодно')
    return res


while True:
    say_rules()
    val = count_attempts(MAX_GUESS)
    counter = 0
    number = get_secret_number()
    while counter < MAX_GUESS:
        player_number = make_player_number(val)
        result = is_number(number, player_number)
        for word in result:
            print(word, end=' ')
        print('\n')
        if player_number == number:
            print(f"Вы победили. Загаданное число действительно: {number}")
            break
        counter += 1
    else:
        print(f"Жаль, но Вы проиграли. Загаданное число было: {number}")
    if input('\n\nХотите сыграть еще раз (Да/Нет?)  ') not in 'yes y да д'.lower().split():
        break
    else:
        clear()
        print('Напомню правила\n\n')

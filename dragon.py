# игра "Царство Дракона"

import random
import time


# Приветствие
def greeting():
    text = ['Вы находитесь в землях, заселенных драконами.',
            'Перед собой вы видите две пещеры.',
            'В одной из них — дружелюбный дракон,',
            'который готов поделиться с вами своими сокровищами.',
            'Во второй — `жадный и голодный дракон, который мигом вас съест.',
            'В какую пещеру вы войдете? (нажмите клавишу 1 или 2)']
    for line in text:
        print(line)
        time.sleep(3)


# Продолжение истории
def cont():
    text = ['Вы приближаетесь к пещере...',
            'Ее темнота заставляет вас дрожать от страха...',
            'Большой дракон выпрыгивает перед вами! Он раскрывает свою пасть и...']
    for line in text:
        print(line)
        time.sleep(3)


def cave():
    try:
        num = int(input())
        if num in [1, 2]:
            return num
        else:
            raise ValueError
    except ValueError:
        print('Необходимо ввести число 1 или 2. Попробуйте еще раз:')
        cave()


# Собственно игра
repeat = 1

while repeat:
    greeting()
    dragon = random.randint(1, 2)
    cave()
    cont()
    time.sleep(5)

    if cave == dragon:
        print('\n...делится своими сокровищами!')
    else:
        print('\n...моментально вас съедает!')

    print('\n\nХотите сыграть еще раз? Да/Нет')
    if input() not in ['Да', 'да', 'д', 'Д', 'Yes', 'yes', 'y', 'Y']:
        repeat = False
        print('\nДо свидания. Спасибо за игру!')

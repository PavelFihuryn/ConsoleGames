# Эта игра по угадыванию чисел.
import random

INF = 20  # Предел загаданного числа
TRY = 5  # Количество попыток


def trying(num: int):
    if num == 1:
        return "попытку"
    elif num >= 5:
        return "попыток"
    else:
        return "попытки"


guesses_taken = 0
guess = 0

print('Привет! Как тебя зовут?')
my_name = input()

number = random.randint(1, 20)
print('Что ж ' + my_name + f', я загадаю число от 1 до {INF}. Попробуй угадать с {TRY} попыток.')

for guesses_taken in range(TRY):
    try:
        guess = int(input('Введи чило: '))
    except ValueError:
        print('Это не число! Попробуй снова.')
        continue

    if INF < guess < 1:
        print(f'Твое число должно быть от 1 до {INF}.Попробуй вновь.')
    elif guess < number:
        print('Твое число слишком маленькое. Попробуй снова.')
    elif guess > number:
        print('Твое число слишком большое. Попробуй ещё разок.')
    elif guess == number:
        break
    else:
        print('Вот это поворот!!! Произошла ошибка. Перезапусти программу снова.')

if guess == number:
    guesses_taken = str(guesses_taken + 1)
    print('Отлично, ' + my_name + '! Ты справился за ' + guesses_taken + ' ' + trying(int(guesses_taken)))

if guess != number:
    number = str(number)
    print('Увы. Я загадал число ' + number + '.')

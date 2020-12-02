# Подбрось манетку

import random


def trying() -> int:
    result = int(input())
    if result <= 1000:
        return result
    else:
        raise ValueError


print("Я подброшу манетку 1000 раз. Угадай сколько раз выпадет 'Орел'. Для продолжения нажми 'Enter'")
input()

count = 0
i = 0

while i < 1000:
    if random.randint(0, 1) == 1:
        count += 1
    i += 1

print('Как думаешь, сколько Орлов было?')

try:
    res = trying()
except ValueError:
    print('Необходимо ввести число от 1 до 1000. Попробуй еще раз:')
    res = trying()

if res == count:
    print("\nНичего себе! Ты угадал!")
elif res > count:
    print("Немного ошибся. Орлов выпало %d. Разница составила %d" % (count, res - count))
else:
    print("Малость ошибся. Орлов выпало %d. Разница составила %d" % (count, count - res))

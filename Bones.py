#эта прога демоснтрирует генерацию случайных чисел,
#но я уже опробовал эту функцию в предыдущей домашке)
#ладно посыпали - ah shit, here we go again!

import random
input("Нажмите Enter, чтобы бросить кости.")

#создаем случайные числа из диапохона 1-6
diel = random.randint(1, 6)
diel1 = random.randrange(6) + 1
total = diel + diel1
print("\nПри вашем броске выпало", diel, "и", diel1, "очков, в сумме", total)
input("\n\nНажмите Enter, чтобы выйти.")
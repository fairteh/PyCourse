#Home Assignment 2 chapter
#Напишите программу, в окно которой пользователь сможет ввести названия двух своих любимых блюд.
#Программа должна сцеплять две эти строки и выводить полученную строку как название нового невиданного блюда.

from random import randint
name = input("Hey, User! What's your name? ")
print("OK,", name, "Do you like cooking? Do you wanna create something new and incredible?")
print("Well, as the answer 'no' is not accepted) This is your chance to get feel yourself as a chief!")
dish_name_1 = input("\nSo, tell me what's your favourite dish? ")
dish_name_2 = input("What's your second favourite food? ")
key_word = input("You also can put here your special ingredient (ex. socks; dick; spit; etc.): ")
number_1 = randint(0,2)
number_2 = randint(3,5)
number_3 = randint(0,2)
number_4 = randint(3,5)
number_5 = randint(0,2)
number_6 = randint(3,5)


new_dish = dish_name_1[number_1 : number_2] + key_word[number_3 : number_4] + dish_name_2[number_5 : number_6]
print("Ladies and gentelmen! I'm so pleased to present you our new dish created by a special guest:")
print("Chief", name)
print("And the dish is called -", new_dish)

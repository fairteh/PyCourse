#well done Gleb! now you can programm something incorrect
#this program demonstrate logical mistake

print("""
            Рантье
Программа подсчитывает ваши ежемесячные расходы.
Эту статистику нужно знать. чтобы у вас не закончились деньги и вам не пришлось искать работу.
Введите суммы расходов по всем статьям. перечисляемым ниже. Вы богаты - так не мелочитесь. 
Пишите суммы в долларах. Без центов.""")
car = input("\nТехническое обслуживание машины (естественно Ламборгини): ")
rent = input("Аренда роскошного двухэтажного пэнтхауса на Манхэтене: ")
jet = input("Аренда самолета: ")
gifts = input("Подарки: ")
food = input("Личный шеф-повар со звездой мишлен, а также обеды и ужины в дорогих ресторанах: ")
staff = input("Зарплата прислуге: ")
guru = input("Плата личному духовному гуру и ментору: ")
games = input("Дорогие и мощные компьютеры и скины в фортнайте: ")
total = car + rent + jet + gifts + food + staff + guru + games
print("\nОбщая сумма:", total)
input("\n\nНажмите Enter, чтобы продолжить.")

#now let's try with no logic mistakes u such a stupid banana boi
#look and remember

print("""
            Рантье
Программа подсчитывает ваши ежемесячные расходы.
Эту статистику нужно знать. чтобы у вас не закончились деньги и вам не пришлось искать работу.
Введите суммы расходов по всем статьям. перечисляемым ниже. Вы богаты - так не мелочитесь. 
Пишите суммы в долларах. Без центов.""")
car = input("\nТехническое обслуживание машины (естественно Ламборгини): ")
car = int(car)
rent = input("Аренда роскошного двухэтажного пэнтхауса на Манхэтене: ")
rent = int(rent)
jet = int(input("Аренда самолета: "))
gifts = int(input("Подарки: "))
food = int(input("Личный шеф-повар со звездой мишлен, а также обеды и ужины в дорогих ресторанах: "))
staff = int(input("Зарплата прислуге: "))
guru = int(input("Плата личному духовному гуру и ментору: "))
games = int(input("Дорогие и мощные компьютеры и скины в фортнайте: "))
total = car + rent + jet + gifts + food + staff + guru + games
print("\nОбщая сумма:", total)
input("\n\nНажмите Enter, чтобы завершить.")

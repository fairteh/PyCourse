#программа демонстрирует составные условия и логические операторы

print("\tЭксклюзивная компьютерная сеть")
print("\tТолько для зарегестрированных и особых пользователей!\n")
security = 0
username = ""
while not username:
    username = input("Логин: ")
password = ""
while not password:
    password = input("Пароль: ")
if username == "Maxoid" and password == "secret":
    print("Привет, Макс!")
    security = 5
elif username == "Glebasta" and password == "yeahboy":
    print("Здравствуйте, мой господин!")
    security = 3
elif username == "Ar7" and password == "fuckingseniy":
    print("Доброго времени суток, Арсений!")
    security = 3
elif username == "Alex" and password == "dota2":
    print("Саламуалекум, Санечек!")
    security = 3
elif username == "guest" and password == "guest":
    print("Добро пожаловать к нам в гости!")
    security = 1
else:
    print("Войти в систему не удалось. Должно быть, вы не очень-то эксклюзивный гражданин.\n")
input("\n\nНажмите Enter, чтобы выйти.")

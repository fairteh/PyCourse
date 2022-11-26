#Напишите проrрамму «Щедрый посетитель»,
#в окно которой пользователь сможет ввести сумму счета за обед в ресторане.
#программа должна выводить два значения: чаевые из расчета 15 и 20 % от указанной суммы.

print("Hello! I know that you are so generous and wanna give some tips to your slut)")
check = int(input("Just for your convinience type here the price of your slut: "))
per_cents = int(input("Type your preferable amount of percents: "))
tips = (check * per_cents)/100
print("\n", tips, "Nah, she does not deserve it! Give her -", (tips * 10)/100)
input("\nPress Enter to accept")

#home assignment 2
#карочке мне лень копировать, тут про машину, налог, рег. сбор, агентский сбор, доставку

print("I can see that you are getting ready to buy a new car -_-")
price = int(input("\nHow much does it cost? "))
taxes = int((price * 9)/100)
registration = int((price * 4)/100)
tips = int(15000)
delivery = int(40000)
total = price + taxes + registration + tips + delivery
print("\nDo you know that you will pay", taxes, "for 9% taxes,", registration, "registration fee,",
     tips, "cost of agent and", delivery, "for delivery.")
print("Finally, you will shit", total, "$")
input("\nPress enter to stop.")
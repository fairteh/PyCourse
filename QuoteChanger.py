#давайте-ка узнаем как работать со строками
#ща буит мясо и магия всего пайтона воедине
#цитата Томаса Уотсона, который в 1943 г. был директором IBM

quote = "Думаю, на мировом рынке можно будет продать штук пять компьютеров."
print("Исходная цитата:")
print(quote)
print("\nОна же в верхнем регистре:")
print(quote.upper())
print("\nОна же в нижнем регистре:")
print(quote.lower())
print("\nКак заголовок:")
print(quote.title())
print("\nС маааааленькой заменой:")
print(quote.replace("штук пять", "несколько миллионов"))
print("\nА вот опять исходная цитата:")
print(quote)
input("\n\nНажмите Enter, чтобы выйти.")

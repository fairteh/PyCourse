#датчик настроения
#программа демонстрирует использование elif

from random import randint
print("ТЫ знал, что я могу угадать по твоему настроению кто ты из персонажей аниме?")
print("Да да! Я могу распознавать твое настроение через монитор компухтера.")
print("Нет? Давай я тебе продемонстрирую свои способности и расскажу кто ты сегодня из аниме!")
input("\n\nНажми Enter, чтобы погадать.")
character = randint(1, 5)
if character == 1:
    print("\nТы сегодня Усаги Цукино или же Сейлор мун! Беззаботная школьница, которая может \n" \
    + "превращаться в фактически лидера основных героинь сериала, воинов в матросках. Атаки, относящиеся к свету (особенно лунному) и любви.")
    print(""".
░░░░░░░▄████▄░░░░░░░░░░░▄████▄░░░░░░░
░░░░░░██░░░███▀▀██▄██▀▀██▀░░░██░░░░░░
░░░░░░██▄▄██▀░░░░▀▀▀░░░░▀██▄▄██░░░░░░
░░░░░██▀▀█░░░░░░░░░░░░░░░░▀█▀▀██░░░░░
░░░░█▀░▄██▄░░░▄███████▄░░▄███▄░██░░░░
░░░█▀░██▀░▀█▄▄██░░░░░██▄▄█▀░▀█▄░██░░░
░░██░█▀░░░░██▀███░░░███▀██░░░░██░██░░
░██░█▀░░░░░██░▀░█░░░█░▀░█▀░░░░░██░█▄░
▄█░██░░░░░▄▄█▄░▀▀░▄░▀▀░▄█▄▄░░░░░██▀█░
████░▄▄██▀▀▀▀██▄░░█░░▄██▀▀▀▀██▄░░████
███░░░▀██▄░░░▀███▄▄▄███▀░░░▄██▀░░░███
██▀▄███▄░▀█▄▄░▀█▄▀▀▀▄█▀░▄██▀░▄██▄▄▀██
██░▀▀░░█▄░████▄██▄▄██▄▄████░██░░▀▀░██
▀█▄░░░▄█░░██░░░▀█▀░▀█▀░░░█▀░░█▄░░▄▄█░
░░▀▀▀▀▀░░░░█▄▄▄███████▄▄▄█░░░░▀▀▀▀▀░░
░░░░░░░░░░░██▀▀░░░░░░░▀▀██░░░░░░░░░░░
""")
elif character == 2:
    print("\nСегодня ты Сайтама или же Ванпанчмен! Сильнейший герой в своей вселенной. По его словам, он обрёл свою невероятную силу \n" \
    + "выполняя на протяжении нескольких лет тренировку: 100 отжиманий, 100 приседаний, 100 на пресс и 10 км бега, каждый день.\n" \
    + "Во время них он не пользовался кондиционером и питался строго 3 раза в день, в основном бананами, Сайтама тренировался \n" \
    + "даже когда был в предсмертном состоянии, от пережитого стресса его ранее черные пышные волосы, полностью выпали на его голове, оставив лысым.")
    print(""" .
⠄⠄⠄⠄⠄⠄⠄⠄⠄⣀⣤⣤⣤⣤⣤⣤⣤⣤⣤⣀
⠄⠄⠄⠄⠄⠄⣠⡶⠛⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠁⠙⢶⣀
⠄⠄⠄⠄⢀⡼⠋⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠹⣆
⠄⠄⠄⢠⡟⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢹⣆
⠄⠄⢀⡟⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢹⣆
⠄⠄⣾⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢿
⠄⢸⡿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⣇
⠄⢸⣷⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⣿⡽⣆
⠄⠈⣿⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢈⣯⠻⢹⡄
⠄⠄⢸⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣠⣤⣤⡄⠄⠄⠸⣿⠄⢸⡇
⠄⣼⠇⢿⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠴⠾⠛⣡⣤⣴⠶⠆⠄⠄⠟⢠⣿⠁
⠄⣿⠰⡟⣷⠄⠄⣤⣤⣤⣤⣤⣦⡀⠄⠄⠄⠄⣾⡋⣯⠄⣼⠇⠄⢠⣴⡿⠁
⠄⠹⣷⡀⢸⣧⠄⢶⣍⡉⠉⣤⣼⠇⠄⣦⠄⠄⠈⠛⠿⠟⠋⠄⠄⠈⠉
⠄⠄⠈⠻⣦⣹⣆⠄⠉⠻⠶⠟⠋⠄⠄⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⣸⣧⣀
⠄⠄⠄⠄⠘⠛⠻⣦⡀⠄⠄⠄⠄⠄⠄⢸⣇⡀⠄⠄⠄⠄⠄⠄⢰⣿⣿⣿⣿⣦
⠄⠄⠄⠄⠄⠄⠄⠙⣷⣄⠄⠄⠄⠄⠄⠄⠉⠁⠄⠄⠄⠄⠄⢀⣿⣿⣿⣿⣿⣿
⠄⠄⠄⠄⠄⠄⢀⣴⠟⣡⣶⡀⠄⠄⠄⠄⠄⠾⠂⠄⠄⠄⢠⣾⣿⣿⣿⢱⣿⠏
⠄⠄⠄⠄⠄⢠⡙⣵⣿⣿⣿⠿⣷⣤⣀⡀⠄⠄⠄⠄⢀⣴⣿⣿⣿⣿⢣⣿⠏⠄
⠄⠄⠄⠄⢰⡟⠻⠈⠻⣿⣿⣄⡻⠉⠻⣿⣷⣶⣶⣾⣿⣿⣿⣿⣿⢡⣿⠏⡄⠄
⠄⠄⠄⢀⡟⠄⠄⠄⠰⢮⡛⠿⣿⣦⣄⡀⠈⠙⠻⢿⣿⣿⣿⣿⢧⣿⢏⡼⠁⣠
⠄⠄⠄⢸⡇⠄⠄⠄⠄⠄⠙⠲⠌⠛⢿⣏⠠⣤⣤⣶⣾⣿⣿⡟⢠⠇⠈⢀⣶⠟
⠄⠄⣰⠟⠛⠷⣶⣤⣤⣤⣄⡀⠄⢸⣶⣬⣛⠦⠉⠻⢿⣿⡿⠁⠋⠄⣾⣿⣇⠄
⢀⣼⠋⠄⠄⠄⠄⠈⠉⠙⠛⠻⢷⣾⣿⣿⣭⣧⡶⠂⠄⠄⠄⠄⠄⠄⠸⣿⣿⠄
⡾⠁⠄⠄⠄⠄⠄⠄⣀⠄⠄⠄⠄⠄⡌⣿⡃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⣿⠄
⠄⠄⠄⢀⠄⠄⠄⣼⠇⠄⠄⠄⠄⠄⣷⢻⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⣿⡇
⣄⠄⠄⠸⡇⠄⣰⠏⠄⠄⠄⠄⠄⠄⢻⣸⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠛⠓
""")
elif character == 3:
    print("\nТы сегодня Ягами Лайт, также известный как Ки́ра! Очень умный, расчётливый, \n" \
    + "с повышенным чувством справедливости молодой человек.")
    print("\n(соре картиночку не нашел ;3)")
elif character == 4:
    print("\nСегодня ты Монки Д. Люффи! Основатель и капитан Пиратов Соломенной Шляпы, а \n" \
    + "также один из четырёх лучших бойцов. Его мечта — стать Королём Пиратов, и найти \n" \
    + "легендарное сокровище Ван Пис, оставленное покойным Королём Пиратов — Гол Д. Роджером. \n" \
    + "Он верит, что став Королём Пиратов, он станет самым свободным человеком в мире.")
    print(""" .
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠠⠤⠒⠒⠒⠒⠒⠤⣄⡀
⠄⠄⠄⠄⢀⡲⢋⠝⠋⣛⣳⡄⠄⠄⠄⠄⠄⠄⠉⠓⢄
⠄⢀⠠⣴⠗⢀⠥⠂⢁⠤⠤⠤⠁⠄⠄⠄⠄⠄⠄⠄⠄⣛⠛⠉⠗⠒⠲⢤⣀
⠰⠃⠐⠄⠋⡠⠄⠮⠤⠤⠤⠤⡤⡄⠄⠄⠄⠄⠄⠄⢠⣽⠄⠄⠄⠄⠄⠄⢸⡆
⠄⠜⠄⠄⠈⠄⢠⣤⣔⣒⡒⠒⠂⠁⠄⡀⢀⣀⣤⣶⣿⡟⠄⠄⠄⠄⠄⢀⡼
⠈⠄⠄⠄⠄⣰⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠉⠁⠄⠄⠄⢄⡴⠋
⠄⠄⠄⠄⣰⠋⠄⠄⠄⠈⠙⠛⠛⠛⠛⠋⠉⠄⠄⠄⠄⢀⣠⣴⡊⠁
⠄⡠⠐⠉⢸⣶⣄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⡀⣤⣶⣿⣿⣿⡻⡄
⠄⠁⠄⠄⣿⢹⣿⣿⣿⣶⣦⣶⣶⣶⣶⣶⣙⠋⠴⠛⣿⢛⡿⠬⠃
⠄⠄⠄⠄⠈⠘⠹⣿⣿⠛⠛⠛⢿⡇⠄⠉⠄⠘⠉⢰⣯⡊⠙⠄
⠄⠄⠄⠄⠄⠄⠄⠈⠱⡄⠄⠄⠘⠃⠄⠄⠄⠄⠠⠛⠄⠁
⠄⠄⠄⠄⠄⠄⠄⠄⠄⢹⢲⣄⠄⠒⠂⠄⣀⢴
⠄⠄⠄⠄⠄⣀⣀⣀⣀⣈⠄⢻⣿⣶⣴⣾⡟⢸⣀⣀⣀⣀⣀⣀⡀
⠄⠄⠄⢀⡎⠄⢀⣠⡤⠂⢠⠈⢿⣿⡿⣿⠃⠄⠙⣀⣀⣀⡀⠄⠙⣄
⠄⠄⠄⠄⠄⢠⠉⠉⢇⠄⠈⡇⠘⣏⠄⡿⡰⠄⠄⢀⠛⠛⠻⣆⠄⠄⠄
⠄⠄⠄⠄⠄⢸⠉⠉⠉⠗⠒⢿⡀⠸⡈⣠⠧⠞⠉⡏⠉⠉⠉⢹⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠸⠄⠄⠄⠄⠄⠄⠁⠄⠉⠉⠄⠄⠈⠄⠄⠄⠄⠸⠄⠄⠄⠄""")
elif character == 5:
    print ("\nПохоже сегодня вы Наруто Узумаки! Светловолосый и голубоглазый подросток-ниндзя, \n" \
    + "сын бывшего главы деревни Коноха. На животе Наруто находится печать в виде спирали, \n" \
    + "которая проявляется, если сконцентрировать чакру. В печати запечатан Девятихвостый Демон-Лис. \n")
    print(""" _______________________¶_________¶¶
________________¶_____¶_¶_______¶_¶
________¶______¶¶¶¶___¶__¶____¶¶__¶________¶¶
________¶¶¶¶¶__¶¶_¶__¶____¶_¶¶¶___¶¶____¶¶¶¶¶
________¶¶__¶¶¶¶___¶¶¶_____¶¶_____¶¶_¶¶¶¶__¶¶
_________¶_____¶____¶______________¶¶¶_____¶
__________¶________________________________¶
__¶¶¶_¶¶__¶¶______________________________¶¶
__¶¶¶__¶__________________________________¶¶¶¶
____¶¶_______________________________________¶¶¶¶¶
_____¶¶_________________________________________¶¶¶
_______¶¶________________________________¶¶__¶¶¶
___¶¶¶¶¶¶___________________________¶____¶¶¶¶
_¶¶¶_______________________¶¶¶¶¶___¶¶___¶¶¶¶¶
_¶¶___________________¶¶¶¶¶¶¶¶¶¶__¶¶¶___¶¶¶_¶¶
___¶¶¶____________¶¶¶¶¶¶¶¶¶¶_¶¶¶_¶¶¶¶¶_¶¶¶__¶¶¶
____¶¶______¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶_¶¶¶
__¶¶_______¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶¶__¶
_¶¶______¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
_¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶_________¶¶¶¶¶¶¶
______¶¶¶¶¶¶¶¶_____¶¶¶¶_____¶________¶¶¶¶__¶
______¶¶¶¶________¶¶__¶¶___¶¶_________¶¶¶__¶
_______¶¶¶________¶_¶__¶¶__¶___________¶___¶
_______¶¶¶________¶_¶__¶¶_¶¶___¶¶¶¶¶¶_______¶
______¶¶¶¶________¶¶_¶¶¶¶¶¶_¶¶¶¶¶¶___________¶
______¶¶¶¶_________¶¶_¶__¶¶_______¶¶¶_________¶
______¶¶¶¶__________¶¶________¶¶¶¶_________¶¶¶
_____¶¶¶¶¶_________¶__¶¶¶_____¶___¶¶_______¶¶
_____¶¶¶¶¶¶______¶¶¶____¶¶_____¶¶¶_____¶¶¶¶¶
_____¶¶¶¶¶¶___¶¶¶¶¶¶_____¶¶___¶¶__________¶
____¶¶¶¶¶_¶__¶__¶_________¶¶_____________¶
____¶¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶_____________________¶
____¶¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____________¶¶
___¶¶¶¶¶¶_¶¶_¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶
___¶¶¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
___¶¶¶¶¶__¶¶¶¶¶_¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
__¶¶¶_¶¶_¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
__¶¶¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
_¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶¶¶
_¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶
¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
""")
else:
    print("\nПохоже сегодня ваш персонаж отсуствует на месте(")

print("\nПриходи потом! Узнаем кем ты будешь завтра)")
input("Нажми Enter, чтобы выйти.")
import random
from datetime import date
a = ''
films = ['Мстители финал', 'Dungeons and Dragons. Честь среди воров', 'Стражи галактики', 'Красное уведомление', 'Бойцовский клуб']
music_band = ['Imagine Dragons', 'Nirvana', 'Linkin park', 'Skillet', 'Limp Bizkit']
songs_dragons = ['Believer', 'Bad liar', 'Roots']
songs_nirvana = ['Smells Like Teen Spirit', 'Rape me', 'Lithium']
songs_park = ['Breaking the Habit', 'Numb', 'Faint']
songs_skillet = ["Monster", 'Finish line', 'Hero']
songs_bizkit = ['Take a look around', 'My Way', 'Rolling']
while a != "Стоп" and a!= 'стоп':
    print("Привет, это твой персональный помошник Адольфик")
    print("Я могу:")
    print("1. Включить конвертер")
    print("2. Включить калькулятор")
    print("3. Расчитать доходность вклада")
    print("4. Перевести число из различных систем счисления в десятичную")
    print("5. Посоветовать фильм на вечер")
    print("6. Посоветовать группу и одну из её песен.")
    print("7. Назвать сегоднюшнюю дату")
    print("Если вы хотите завершить программу напишите 'Стоп'")
    print("Введитье номер операции, которую хотите выполнить:")
    a = input()

    if int(a) == 1:
        print("Эта программа умеет:")
        print("1. Переводить из грамм в килограммы")
        print("2. Переводить из килограмм в граммы")
        print("3. Переводить из сантиметров в метры")
        print("4. Переводить из метров в сантиметры")
        number1 = int(input(("Введите число, которое хотите конвертировать:")))
        operation = int(input("Введите номер операции"))
        if operation == 1:  # Операция сравнивается с её номером и выполняется соотвецтвенное действие, вслед за чем происходит вывод итога данной операции
            print(number1 / 100)
        elif operation == 2:
            print(number1 * 100)
        elif operation == 3:
            print(number1 / 100)
        elif operation == 4:
            print(number1 * 100)

    elif int(a) == 2:
        number1 = int(input("Введите 1-е число:"))  # Ввод первого числа
        number2 = int(input("Введите 2-е число:"))  # Ввод второго числа
        print("Эта программа умеет:")  # пердставляется выбор операций
        print("1. Уиножать")
        print("2. Делить")
        print("3. Вычислять остаток от деления")
        print("4. Выполнять целочисленное деление")
        print("5. Возводить в степень")
        print("6. ")
        print("5. Возводить в степень")
        operation = input("Введите номер операции: ")
        if operation == 1:  # Операция сравнивается с её номером и выполняется соотвецтвенное действие, вслед за чем происходит вывод итога данной операции
            print(number1 * number2)
        elif operation == 2:
            print(number1 / number2)
        elif operation == 3:
            print(number1 % number2)
        elif operation == 4:
            print(number1 // number2)
        elif operation == 5:
            print(number1 ** number2)


    elif int(a) == 3:
        number1 = int(input("Введите сумму вклада:"))
        number2 = int(input("Введите срок вклада:"))
        number3 = int(input("Введите процент вклада:"))
        number12 = number1
        for x in range(number2):
            number1 = number1 + number1 * 0.01 * number3 / number2
        income = number1 - number12
        print(income)


    elif int(a) == 4:
        numder1 = int(input(("Введите число которое хотите перевести в деятичную систему счисления:")))
        numder2 = int(input("Введите систему счисления вашего числа:"))
        print(int(numder1, numder2))
    elif int(a) == 5:
        g = random.randint(0, len(films) - 1)
        print("Сегодня вечером я рекомендудую вам посмотреть:", films[g])
    elif int(a) == 6:
        p = random.randint(0, len(music_band) - 1)
        band = music_band[p]
        if band == "Limp Bizkit":
            song = songs_bizkit[random.randint(0, len(songs_bizkit) - 1)]
        elif band == "Imagine Dragons":
            song = songs_dragons[random.randint(0, len(songs_dragons) - 1)]
        elif band == "Linkin park":
            song = songs_park[random.randint(0, len(songs_park) - 1)]
        elif band == "Nirvana":
            song = songs_nirvana[random.randint(0, len(songs_nirvana) - 1)]
        elif band == "Skillet":
            song = songs_skillet[random.randint(0, len(songs_skillet) - 1)]
        print("Сегодня я рекомендую вам послушать песню", song, 'замечательной группы', band)
    elif int(a) == 7:
        current_date = date.today()
        print(current_date)
    a = input("Если хотитие продолжить и вернуться к списку операций, то введите любое число или букву, если же хотите остановится, то напишите 'Стоп'")
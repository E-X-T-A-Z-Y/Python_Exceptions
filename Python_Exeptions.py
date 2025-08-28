import random



jokes = [
    "— Лікарю, у мене дві проблеми... — Які? — Памʼять і... другу забув.",
    "Адмін — як чарівник: коли все працює, ніхто не помічає.",
    "Падає програма. — Чому? — Бо їй сумно без тестів.",
    "Код без багів — це як єдиноріг: усі чули, ніхто не бачив.",
    """Програмісту:
– Вибачите, можна вам одне питання?
– Можна. І ви його вже запитали.""",
    "Інтернет – він такий. Читаєш коментарі, думаєш: “Одні ідіоти!” Починаєш з ними сперечатися й не помічаєш, як на одного ідіота стало більше.",
    "Майстерність програміста не в тому, щоб писати програми, котрі працюють без помилок, а в тому, щоб писати програми, котрі працюють за будь-якої кількості помилок.",
    """– Чим відрізняється програміст від політика?
– Програмісту платять гроші за програми, що працюють.""",
    """Програміст після напруженого трудового дня заглядає в холодильник, бере пачку масла, читає на обгортці: “Масло вершкове. 72%”.
У голові майнула думка: “О! Скоро завантажиться!”
Кладе масло в холодильник. Зачиняє двері""",

]
pool = []

def take_joke():
    global pool
    if not jokes:                      # на всяк випадок
        return "(жартів немає)"
    if not pool:                       # якщо пул порожній — перезбираємо
        pool = jokes[:]                # копія
        random.shuffle(pool)           # перемішати
    return pool.pop()



#Task_1

while True:
    try:
        numOne = float(input("Перше число: "))
        numTwo = float(input("Друге число: "))
        division = (numOne /  numTwo)
        print(f"Результат ділення: {division:.4f}")
        if numOne == 0:
            break

    except ValueError:
        print("Значення не є числом")
        continue

    except ZeroDivisionError:
            print("Ділити на нуль не можна!!!!!!")
            continue

    finally:
        print("Анекдот:", take_joke())
    if input("Ще раз? (y/n): ").strip().lower() != "y":
        break

#Task_2

arr = [10,20,30,40,50,60,70,80,90,100]

while True:
    try:
        idx = int(input("Введіть індекс елемента: "))
        value = arr[idx]
        print(f"Елемент за індексом: {value}")
    except ValueError:
        print("Індекс має бути цілим числом!")
        continue
    except IndexError:
        print("Індекс виходить за межі списку!")
        continue
    finally:
        print("Анекдот:", take_joke())
    if input("Ще раз? (y/n): ").strip().lower() != "y":
        break

#Task_3

while True:
    try:
        parts = (input("Введіть числа через пробіл:").split())
        numbers = list(map(float, parts))
        total = sum(numbers)
        print(f"Загальна сума: {total}")

    except ValueError:
        print("Введені повині бути числа через пробіл!!!")
        continue
    finally:
        print("Анекдот:", take_joke())
    if input("Ще раз? (y/n): ").strip().lower() != "y":
        break


# #Task_4

while True:
    try:
        num = float(input("Число для рахунку квадратного коріня: "))
        if num < 0 :
            print("Число не можу бути від'ємним!!!")
            continue
        else:
            root = num ** 0.5
            print(f"Корінь виходить: {root:.4f}")
            if input("Ще раз? (y/n): ").strip().lower() != "y":
                break
    except ValueError:
        print("Значення не є числом")
        continue
    finally:
        print("Анекдот:", take_joke())

#Task_5

while True:
    try:
        infoGoods = input("Вкажіть через пробіл назву товару, ціну й кількість: ")
        partsGoods = infoGoods.split()
        if len (partsGoods) != 3:
            print("Некоректні дані повинно бути вказано, назву, ціну, кількість!!! ")
            continue
        nameGoods = partsGoods[0].strip()
        priceGoods = float(partsGoods[1].strip())
        amountGoods = int(partsGoods[2].strip())
        if priceGoods < 0 or amountGoods < 0:
            print("Ціна й кількість не можуть бути від'ємні!!!")
            continue
        print(f"Назва: {nameGoods}, Ціна: {priceGoods}, Кількість: {amountGoods}")
        if input("Ще раз? (y/n): ").strip().lower() != "y":
            break
    except ValueError:
        print("Некоректні дані")
    finally:
        print("Анекдот:", take_joke())




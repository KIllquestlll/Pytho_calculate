import math

def calculate(first, sign, second=0):
    sign = sign.lower()

    if sign in ("+", "сложение", "1"):
        print(first + second)
    elif sign in ("-", "вычитание", "2"):
        print(first - second)
    elif sign in ("*", "умножение", "3"):
        print(first * second)
    elif sign in ("/", "деление", "4"):
        if second == 0:
            print("делить на ноль нельзя!")
        else:
            print(first / second)
    elif sign in ("%", "вычисление процента от числа", "5"):
        print(second * first / 100)
    elif sign in ("^", "возведение в степень", "6"):
        print(first ** second)
    elif sign in ("!", "факториал", "7"):
        print(math.factorial(first))
    elif sign in ("sin", "синус", "8"):
        print(math.sin(first))
    elif sign in ("cos", "косинус", "9"):
        print(math.cos(first))
    elif sign in ("tan", "тангенс", "10"):
        print(math.tan(first))


def main():
    while True:

        print("1.Сложение.")
        print("2.Вычитание.")
        print("3.Умножение.")
        print("4.Деление.")
        print("5.Вычисление процента от числа.")
        print("6.Возведение в степень.")
        print("7.Факториал.")
        print("8.Синус.")
        print("9.Косинус.")
        print("10.Тангенс.")
        print("11.Выход.")

        try:
            choice = input("Выберите действие: ")
            one_number = float(input("Введите первое число: "))
            if choice in ("!", "sin", "cos", "tan", "7", "8", "9", "10"):
                calculate(one_number, choice)
            else:
                two_number = float(input("Второе число: "))
            calculate(one_number, choice, two_number)
        except ValueError:
            print("Введен неверный тип данных!")


main()
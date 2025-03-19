import math

def calculate(first, sign, second=None):

    sign = sign.lower()

    try:
        if sign in ("+", "сложение", "1"):
            return first + second
        elif sign in ("-", "вычитание", "2"):
            return first - second
        elif sign in ("*", "умножение", "3"):
            return first * second
        elif sign in ("/", "деление", "4"):
            if second == 0:
                return "Ошибка: Делить на ноль нельзя!"
            return first / second
        elif sign in ("%", "вычисление процента от числа", "5"):
            return second * first / 100
        elif sign in ("^", "возведение в степень", "6"):
            return first ** second
        elif sign in ("!", "факториал", "7"):
            if first < 0:
                return "Ошибка: Число должно быть положительным!"
            return math.factorial(int(first))
        elif sign in ("sin", "синус", "8"):
            return math.sin(math.radians(first))
        elif sign in ("cos", "косинус", "9"):
            return math.cos(math.radians(first))
        elif sign in ("tan", "тангенс", "10"):
            if first % 180 == 90:
                return "Ошибка: Тангенс 90 градусов не определён!"
            return math.tan(math.radians(first))
        else:
            return "Ошибка: Неверная операция!"
    except Exception as error:
        return f"Ошибка: {error}"

def main():
    while True:
        print("\nВыберите операцию:")
        print("1. Сложение (+)")
        print("2. Вычитание (-)")
        print("3. Умножение (*)")
        print("4. Деление (/)")
        print("5. Вычисление процента от числа (%)")
        print("6. Возведение в степень (^)")
        print("7. Факториал (!)")
        print("8. Синус (sin)")
        print("9. Косинус (cos)")
        print("10. Тангенс (tan)")
        print("11. Выход")

        choice = input("Выберите действие: ")

        try:
            if choice in ("7", "8", "9", "10", "!", "факториал", "sin", "cos", "tan"):
                one_number = float(input("Введите число: "))
                result = calculate(one_number, choice)
            elif choice in ("11","выход"):
                print("Завершение работы...")
                break
            else:
                one_number = float(input("Введите первое число: "))
                two_number = float(input("Введите второе число: "))
                result = calculate(one_number, choice, two_number)

            print("Результат:", result)
        except ValueError:
            print("Ошибка: Введены некорректные данные! Попробуйте снова.")

if __name__ == "__main__":
    main()

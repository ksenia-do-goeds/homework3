import math
import statistics

def add(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Оба значения должны быть числом.")
    return a + b

def subtract(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Оба значения должны быть числом.")
    return a - b

def multiply(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Оба значения должны быть числом.")
    return a * b

def divide(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Оба значения должны быть числом.")
    if b == 0:
        raise ZeroDivisionError("На ноль делить нельзя.")
    return a / b

def power(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Оба значения должны быть числом.")
    return a ** b

def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Факториал может быть рассчитан только для неотрицательных целых чисел.")
    return math.factorial(n)

def sine(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Значение должно быть числом.")
    return math.sin(x)

def median(numbers):
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("Все элементы должны быть числами.")
    return statistics.median(numbers)

def calculator():
    print("Доступные операции:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Возведение в степень")
    print("6. Факториал")
    print("7. Синус")
    print("8. Медиана")
    print("--------------------")

    while True:
        operation = input("Операция (или напишите 'exit' для выхода): ")
        if operation.lower() == 'exit':
            break
        
        try:
            if operation == '1':
                a = float(input("Слагаемое 1: "))
                b = float(input("Слагаемое 2: "))
                result = add(a, b)
            elif operation == '2':
                a = float(input("Уменьшаемое: "))
                b = float(input("Вычитаемое: "))
                result = subtract(a, b)
            elif operation == '3':
                a = float(input("Множитель 1: "))
                b = float(input("Множитель 2: "))
                result = multiply(a, b)
            elif operation == '4':
                a = float(input("Делимое: "))
                b = float(input("Делитель: "))
                result = divide(a, b)
            elif operation == '5':
                a = float(input("Число: "))
                b = float(input("Степень: "))
                result = power(a, b)
            elif operation == '6':
                n = int(input("Введите неотрицательное целое число: "))
                result = factorial(n)
            elif operation == '7':
                x = float(input("Введите значение: "))
                result = sine(x)
            elif operation == '8':
                numbers = list(map(float, input("Список чисел: ").split()))
                result = median(numbers)
            else:
                print("Неверная операция.")
                continue
                
            print(f">>> {result}")
        except (TypeError, ZeroDivisionError, ValueError) as e:
            print(f"Ошибка: {e}")

if __name__ == "__main__":
    calculator()

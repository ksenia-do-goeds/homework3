from typing import List

def multiply_elements(numbers: List[int], multiplier: int = 2) -> List[int]:
    return [number * multiplier for number in numbers]

def multiply_elements_lambda(numbers: List[int], multiplier: int = 2) -> List[int]:
    return list(map(lambda x: x * multiplier, numbers))

if __name__ == "__main__":
    user_input = input("Введите список чисел через пробел: ")
    numbers = list(map(int, user_input.split()))
    
    multiplier_input = input("Введите множитель (по умолчанию 2): ")
    multiplier = int(multiplier_input) if multiplier_input else 2

    result_function = multiply_elements(numbers, multiplier)
    result_lambda = multiply_elements_lambda(numbers, multiplier)

    print(f"Результат (функция): {result_function}")
    print(f"Результат (лямбда-функция): {result_lambda}")

"""Задача 1. Палиндром — проверка числа без использования строк.

Подробное объяснение, сложность и визуализация:
см. README_объяснение_сложность_визуализация.md
"""


def is_palindrome(n: int) -> bool:
    """Проверяет, является ли целое положительное число палиндромом.
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError(f"Ожидалось целое число, получено: {type(n).__name__}")

    # Согласно условию, проверяются целые положительные числа (n > 0)
    if n <= 0:
        return False

    # Числа > 0, оканчивающиеся на 0, палиндромами быть не могут
    if n % 10 == 0:
        return False

    original = n
    current = n
    reversed_num = 0

    while current > 0:
        digit = current % 10
        reversed_num = reversed_num * 10 + digit
        current //= 10

    return original == reversed_num


if __name__ == "__main__":
    test_values = [121, 31, 7, 10, 1221, 12321, 12345, 1000000001]
    print("Демонстрация работы функции is_palindrome:")
    for val in test_values:
        res = is_palindrome(val)
        print(f"  Вход: {val:<10} -> Палиндром: {res}")

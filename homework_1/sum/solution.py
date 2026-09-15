"""Задача 2. Сумма — максимальная сумма элементов, делящаяся на 2.

Подробное объяснение, сложность и визуализация:
см. README_объяснение_сложность_визуализация.md
"""

from typing import Iterable, Union


def max_even_sum(numbers: Union[str, Iterable[int]]) -> int:
    """Находит максимальную сумму элементов массива, которая делится на 2.
    """
    if isinstance(numbers, str):
        tokens = numbers.strip().split()
        if not tokens:
            return 0
        try:
            nums = [int(token) for token in tokens]
        except ValueError as err:
            raise ValueError(f"Ошибка при преобразовании в целое число: {err}") from err
    elif isinstance(numbers, Iterable):
        nums = list(numbers)
    else:
        raise TypeError(
            f"Ожидалась строка или список чисел, получено: {type(numbers).__name__}"
        )

    if not nums:
        return 0

    total_sum = 0
    min_odd: Union[int, None] = None

    for x in nums:
        if not isinstance(x, int) or isinstance(x, bool):
            raise TypeError(f"Элемент массива должен быть целым числом, получено: {x!r}")
        if x <= 0:
            raise ValueError(f"Числа должны быть положительными (> 0), получено: {x}")

        total_sum += x
        if x % 2 != 0:
            if min_odd is None or x < min_odd:
                min_odd = x

    # Если общая сумма уже четная — берем все элементы
    if total_sum % 2 == 0:
        return total_sum

    # Если общая сумма нечетная, исключаем минимальное нечетное число
    if min_odd is not None:
        return total_sum - min_odd

    return 0


if __name__ == "__main__":
    examples = [
        "5 7 13 2 14",
        "3",
        "2 4 6 8",
        "1 3 5",
        "10 20 30 1",
    ]
    print("Демонстрация работы функции max_even_sum:")
    for ex in examples:
        ans = max_even_sum(ex)
        print(f"  Вход: {ex:<18} -> Выход: {ans}")

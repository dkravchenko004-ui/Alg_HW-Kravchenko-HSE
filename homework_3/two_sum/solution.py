"""Задача 1. Two sum — индексы двух чисел с суммой k.

Подробное объяснение, сложность и визуализация:
см. README.md
"""

from typing import Iterable, List, Sequence, Union


def _to_int_list(seq: Union[str, Sequence[int], Iterable[int]]) -> List[int]:
    if isinstance(seq, str):
        tokens = seq.strip().split()
        if not tokens:
            raise ValueError("массив не должен быть пустым")
        try:
            values = [int(token) for token in tokens]
        except ValueError as err:
            raise ValueError(f"ошибка при преобразовании в целое число: {err}") from err
        return values

    if isinstance(seq, Iterable) and not isinstance(seq, (bytes, bytearray)):
        values = list(seq)
    else:
        raise TypeError(
            f"ожидалась строка или последовательность чисел, получено: {type(seq).__name__}"
        )

    if len(values) < 2:
        raise ValueError("в массиве должно быть хотя бы два элемента")

    for item in values:
        if not isinstance(item, int) or isinstance(item, bool):
            raise TypeError(f"элементы должны быть целыми числами, получено: {item!r}")
    return values


def two_sum(arr: Union[str, Sequence[int], Iterable[int]], k: int) -> str:
    """Возвращает два индекса через пробел (по возрастанию), сумма элементов равна k."""
    if not isinstance(k, int) or isinstance(k, bool):
        raise TypeError(f"k должно быть целым числом, получено: {type(k).__name__}")

    nums = _to_int_list(arr)
    seen = {}

    for i, value in enumerate(nums):
        need = k - value
        if need in seen:
            left, right = seen[need], i
            return f"{left} {right}"
        seen[value] = i

    raise ValueError("пара с суммой k не найдена")


if __name__ == "__main__":
    examples = [
        ([1, 3, 4, 10], 7),
        ([5, 5, 1, 4], 10),
        ("2 7 11 15", 9),
        ([-3, 1, 4], 1),
    ]
    print("Демонстрация работы функции two_sum:")
    for arr, k in examples:
        print(f"  arr={arr}, k={k} -> {two_sum(arr, k)}")

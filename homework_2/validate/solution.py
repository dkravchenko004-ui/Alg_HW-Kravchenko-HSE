"""Задача 2. Validate — можно ли получить popped операциями push/pop.

Подробное объяснение, сложность и визуализация:
см. README.md
"""

from typing import Iterable, List, Sequence, Union


def _to_int_list(seq: Union[str, Sequence[int], Iterable[int]], name: str) -> List[int]:
    """Приводит вход к списку целых чисел."""
    if isinstance(seq, str):
        tokens = seq.strip().split()
        if not tokens:
            raise ValueError(f"{name}: последовательность не должна быть пустой")
        try:
            values = [int(token) for token in tokens]
        except ValueError as err:
            raise ValueError(f"{name}: ошибка при преобразовании в целое число: {err}") from err
        return values

    if isinstance(seq, Iterable) and not isinstance(seq, (bytes, bytearray)):
        values = list(seq)
    else:
        raise TypeError(
            f"{name}: ожидалась строка или последовательность чисел, получено: {type(seq).__name__}"
        )

    if not values:
        raise ValueError(f"{name}: последовательность не должна быть пустой")

    for item in values:
        if not isinstance(item, int) or isinstance(item, bool):
            raise TypeError(f"{name}: элементы должны быть целыми числами, получено: {item!r}")
    return values


def validate(
    pushed: Union[str, Sequence[int], Iterable[int]],
    popped: Union[str, Sequence[int], Iterable[int]],
) -> bool:
    """Возвращает True, если popped получается из pushed операциями push и pop."""
    pushed_vals = _to_int_list(pushed, "pushed")
    popped_vals = _to_int_list(popped, "popped")

    n = len(pushed_vals)
    if n != len(popped_vals):
        raise ValueError("pushed и popped должны быть одинаковой длины")
    if n > 100000:
        raise ValueError("длина последовательности не должна превышать 100000")

    stack: List[int] = []
    pop_index = 0

    for value in pushed_vals:
        stack.append(value)
        while stack and stack[-1] == popped_vals[pop_index]:
            stack.pop()
            pop_index += 1

    return pop_index == n


if __name__ == "__main__":
    examples = [
        ("1 2 3 4 5", "1 3 5 4 2"),
        ("1 2 3", "3 1 2"),
        ("1 2 3", "1 2 3"),
        ("1 2 3", "3 2 1"),
    ]
    print("Демонстрация работы функции validate:")
    for pushed, popped in examples:
        result = validate(pushed, popped)
        print(f"  pushed={pushed:<11} popped={popped:<11} -> {result}")

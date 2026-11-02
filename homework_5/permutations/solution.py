"""Задача 2. Все перестановки массива.

Рекурсия обёрнута декоратором trace из задачи 1.

Подробное объяснение, сложность и визуализация:
см. README.md
"""

from typing import Iterable, List, Sequence, Union

from homework_5.tracer.solution import trace


def _to_list(nums: Union[Sequence, Iterable]) -> list:
    if isinstance(nums, (str, bytes, bytearray)):
        raise TypeError(
            f"ожидалась последовательность элементов, получено: {type(nums).__name__}"
        )
    if not isinstance(nums, Iterable):
        raise TypeError(
            f"ожидалась последовательность элементов, получено: {type(nums).__name__}"
        )
    return list(nums)


def permute(nums: Union[Sequence, Iterable]) -> List[list]:
    """Возвращает все перестановки. Порядок — как в примерах условия."""
    values = _to_list(nums)
    n = len(values)
    used = [False] * n

    @trace
    def generate(path):
        if len(path) == n:
            return [list(path)]
        found = []
        for i in range(n):
            if used[i]:
                continue
            used[i] = True
            found.extend(generate(path + [values[i]]))
            used[i] = False
        return found

    return generate([])


if __name__ == "__main__":
    print("перестановки [1, 2, 3]:")
    print(permute([1, 2, 3]))

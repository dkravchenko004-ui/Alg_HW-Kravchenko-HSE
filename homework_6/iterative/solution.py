"""Задача 2. Итеративные mergesort и quicksort.

Подробное объяснение, сложность и визуализация:
см. README.md
"""

from typing import Iterable, List, Sequence, Union


def _to_int_list(seq: Union[Sequence, Iterable]) -> List[int]:
    if isinstance(seq, (str, bytes, bytearray)):
        raise TypeError(
            f"ожидалась последовательность целых, получено: {type(seq).__name__}"
        )
    if not isinstance(seq, Iterable):
        raise TypeError(
            f"ожидалась последовательность целых, получено: {type(seq).__name__}"
        )
    values = list(seq)
    for item in values:
        if not isinstance(item, int) or isinstance(item, bool):
            raise TypeError(
                f"элементы должны быть целыми числами, получено: {item!r}"
            )
    return values


def _merge(a: List[int], aux: List[int], lo: int, mid: int, hi: int) -> None:
    i, j = lo, mid
    for k in range(lo, hi):
        if i < mid and (j >= hi or a[i] <= a[j]):
            aux[k] = a[i]
            i += 1
        else:
            aux[k] = a[j]
            j += 1
    a[lo:hi] = aux[lo:hi]


def _partition(a: List[int], lo: int, hi: int) -> int:
    """Опорный — последний. Меньше него — слева, больше или равные — справа."""
    pivot = a[hi]
    i = lo
    for j in range(lo, hi):
        if a[j] < pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[hi] = a[hi], a[i]
    return i


def mergesort_iterative(nums: Union[Sequence, Iterable]) -> List[int]:
    """Слияние снизу вверх: куски длины 1, 2, 4, ..."""
    a = _to_int_list(nums)
    n = len(a)
    if n <= 1:
        return a
    aux = a[:]
    width = 1
    while width < n:
        for lo in range(0, n, 2 * width):
            mid = min(lo + width, n)
            hi = min(lo + 2 * width, n)
            if mid < hi:
                _merge(a, aux, lo, mid, hi)
        width *= 2
    return a


def quicksort_iterative(nums: Union[Sequence, Iterable]) -> List[int]:
    """Тот же quicksort, стек вместо рекурсии."""
    a = _to_int_list(nums)
    n = len(a)
    if n <= 1:
        return a
    stack = [(0, n - 1)]
    while stack:
        lo, hi = stack.pop()
        if lo >= hi:
            continue
        p = _partition(a, lo, hi)
        stack.append((lo, p - 1))
        stack.append((p + 1, hi))
    return a


if __name__ == "__main__":
    sample = [5, 2, 8, 1, 3]
    print("mergesort_iterative:", mergesort_iterative(sample))
    print("quicksort_iterative:", quicksort_iterative(sample))

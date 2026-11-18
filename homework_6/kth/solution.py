"""Задача 3. k-й по величине элемент, quickselect.

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


def _require_k(k: object) -> int:
    if not isinstance(k, int) or isinstance(k, bool):
        raise TypeError(f"k должно быть целым числом, получено: {type(k).__name__}")
    return k


def _partition(a: List[int], lo: int, hi: int) -> int:
    """Как на лекции: меньше опорного слева, больше или равные справа."""
    pivot = a[hi]
    i = lo
    for j in range(lo, hi):
        if a[j] < pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[hi] = a[hi], a[i]
    return i


def kth_largest(nums: Union[Sequence, Iterable], k: int) -> int:
    """k-й по убыванию элемент. k=1 — максимум. Массив целиком не сортируем."""
    a = _to_int_list(nums)
    k = _require_k(k)
    n = len(a)
    if n == 0:
        raise ValueError("массив пуст")
    if k < 1 or k > n:
        raise ValueError(f"k должно быть от 1 до {n}, получено: {k}")

    target = n - k
    lo, hi = 0, n - 1
    while lo <= hi:
        p = _partition(a, lo, hi)
        if p == target:
            return a[p]
        if p > target:
            hi = p - 1
        else:
            lo = p + 1
    raise ValueError("элемент не найден")


if __name__ == "__main__":
    print(kth_largest([3, 2, 1, 5, 6, 4], 2))
    print(kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))

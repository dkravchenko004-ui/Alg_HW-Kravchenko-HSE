"""Задача 1. Рекурсивные mergesort и quicksort, декоратор времени.

Подробное объяснение, сложность и визуализация:
см. README.md
"""

import time
from functools import wraps
from typing import Any, Callable, Iterable, List, Sequence, Union


def timed(func: Callable) -> Callable:
    """Замеряет время вызова. После работы смотри `func.last_time` (секунды)."""

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.perf_counter()
        try:
            result = func(*args, **kwargs)
        finally:
            wrapper.last_time = time.perf_counter() - start
        return result

    wrapper.last_time = 0.0
    return wrapper


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


def _mergesort(a: List[int], aux: List[int], lo: int, hi: int) -> None:
    if hi - lo <= 1:
        return
    mid = (lo + hi) // 2
    _mergesort(a, aux, lo, mid)
    _mergesort(a, aux, mid, hi)
    _merge(a, aux, lo, mid, hi)


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


def _quicksort(a: List[int], lo: int, hi: int) -> None:
    if lo >= hi:
        return
    p = _partition(a, lo, hi)
    _quicksort(a, lo, p - 1)
    _quicksort(a, p + 1, hi)


@timed
def mergesort(nums: Union[Sequence, Iterable]) -> List[int]:
    """Рекурсивный mergesort. Исходную последовательность не меняет."""
    a = _to_int_list(nums)
    _mergesort(a, a[:], 0, len(a))
    return a


@timed
def quicksort(nums: Union[Sequence, Iterable]) -> List[int]:
    """Рекурсивный quicksort. Опорный — последний элемент текущего отрезка."""
    a = _to_int_list(nums)
    if a:
        _quicksort(a, 0, len(a) - 1)
    return a


if __name__ == "__main__":
    sample = [5, 2, 8, 1, 3]
    print("mergesort:", mergesort(sample), f"time={mergesort.last_time:.6f}s")
    print("quicksort:", quicksort(sample), f"time={quicksort.last_time:.6f}s")
    ordered = list(range(400))
    mergesort(ordered)
    t_m = mergesort.last_time
    quicksort(ordered)
    t_q = quicksort.last_time
    print(f"sorted n=400  mergesort={t_m:.6f}s  quicksort={t_q:.6f}s")

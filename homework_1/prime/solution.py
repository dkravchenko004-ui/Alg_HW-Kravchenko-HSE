"""Задача 3. Простые числа — количество простых строго меньше N.

Подробное объяснение, сложность и визуализация:
см. README_объяснение_сложность_визуализация.md
"""


def count_primes(n: int) -> int:
    """Возвращает количество простых чисел строго меньших N.
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError(f"Ожидалось целое число, получено: {type(n).__name__}")

    # Простых чисел, меньших 2, нет
    if n <= 2:
        return 0

    # is_prime[i] = True, если число i потенциально простое
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False

    p = 2
    while p * p < n:
        if is_prime[p]:
            # Вычеркиваем числа, кратные p, начиная с p * p
            for multiple in range(p * p, n, p):
                is_prime[multiple] = False
        p += 1

    return sum(is_prime)


if __name__ == "__main__":
    examples = [10, 1, 2, 3, 5, 11, 20, 100]
    print("Демонстрация работы функции count_primes:")
    for ex in examples:
        ans = count_primes(ex)
        print(f"  N = {ex:<5} -> Количество простых чисел < N: {ans}")

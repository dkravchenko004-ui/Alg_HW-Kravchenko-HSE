"""Тесты для задачи 3: Подсчет количества простых чисел строго меньших N."""

import unittest
from homework_1.prime.solution import count_primes


class TestCountPrimes(unittest.TestCase):
    """Набор тестов для проверки функции count_primes."""

    # 1. Примеры из условия задачи
    def test_examples_from_description(self):
        """Проверка примеров, указанных в условии."""
        self.assertEqual(count_primes(10), 4)
        self.assertEqual(count_primes(1), 0)

    # 2. Граничные случаи: N <= 2
    def test_edge_cases_non_positive_and_small(self):
        """Граничные случаи для неположительных и малых чисел."""
        self.assertEqual(count_primes(-10), 0)
        self.assertEqual(count_primes(-1), 0)
        self.assertEqual(count_primes(0), 0)
        self.assertEqual(count_primes(2), 0)  # строго меньших 2 нет
        self.assertEqual(count_primes(3), 1)  # только число 2

    # 3. Граничные случаи: N совпадает с простым числом (строгое неравенство < N)
    def test_strictly_less_than_n_when_n_is_prime(self):
        """Проверка, что число N само не включается, если оно простое."""
        self.assertEqual(count_primes(5), 2)
        self.assertEqual(count_primes(7), 3)
        self.assertEqual(count_primes(11), 4)
        self.assertEqual(count_primes(13), 5)

    # 4. Проверка значений сразу после простых чисел
    def test_after_prime_numbers(self):
        """Проверка значений N, следующих сразу за простыми."""
        self.assertEqual(count_primes(4), 2)   # 2, 3
        self.assertEqual(count_primes(6), 3)   # 2, 3, 5
        self.assertEqual(count_primes(8), 4)   # 2, 3, 5, 7
        self.assertEqual(count_primes(12), 5)  # 2, 3, 5, 7, 11
        self.assertEqual(count_primes(14), 6)  # 2, 3, 5, 7, 11, 13

    # 5. Типичные и известные математические значения функции pi(x)
    def test_known_prime_counts(self):
        """Сравнение с эталонными математическими значениями функции pi(x)."""
        self.assertEqual(count_primes(20), 8)
        self.assertEqual(count_primes(30), 10)
        self.assertEqual(count_primes(50), 15)
        # Количество простых чисел < 100 равно pi(99) = 25
        self.assertEqual(count_primes(100), 25)
        # Количество простых чисел < 1000 равно pi(999) = 168
        self.assertEqual(count_primes(1000), 168)
        # Количество простых чисел < 10000 равно pi(9999) = 1229
        self.assertEqual(count_primes(10000), 1229)

    # 6. Обработка некорректных типов данных
    def test_invalid_types(self):
        """Проверка реакции на некорректные типы входных данных."""
        with self.assertRaises(TypeError):
            count_primes(10.5)
        with self.assertRaises(TypeError):
            count_primes("10")
        with self.assertRaises(TypeError):
            count_primes(True)
        with self.assertRaises(TypeError):
            count_primes(None)
        with self.assertRaises(TypeError):
            count_primes([10])


if __name__ == "__main__":
    unittest.main()

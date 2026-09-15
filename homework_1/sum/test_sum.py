"""Тесты для задачи 2: Максимальная четная сумма элементов массива."""

import unittest
from homework_1.sum.solution import max_even_sum


class TestMaxEvenSum(unittest.TestCase):
    """Набор тестов для проверки функции max_even_sum."""

    # 1. Примеры из условия задачи
    def test_examples_from_description(self):
        """Проверка примеров, указанных в условии."""
        self.assertEqual(max_even_sum("5 7 13 2 14"), 36)
        self.assertEqual(max_even_sum([5, 7, 13, 2, 14]), 36)

        self.assertEqual(max_even_sum("3"), 0)
        self.assertEqual(max_even_sum([3]), 0)

    # 2. Граничные случаи: один элемент
    def test_single_element(self):
        """Массивы из одного элемента."""
        self.assertEqual(max_even_sum("4"), 4)  # один четный
        self.assertEqual(max_even_sum("7"), 0)  # один нечетный
        self.assertEqual(max_even_sum([2]), 2)
        self.assertEqual(max_even_sum([9]), 0)

    # 3. Граничный случай: пустой ввод
    def test_empty_input(self):
        """Пустая строка или пустой список возвращают 0."""
        self.assertEqual(max_even_sum(""), 0)
        self.assertEqual(max_even_sum("   "), 0)
        self.assertEqual(max_even_sum([]), 0)
        self.assertEqual(max_even_sum(()), 0)

    # 4. Все элементы четные
    def test_all_even(self):
        """Если все элементы четные, берется сумма всех элементов."""
        self.assertEqual(max_even_sum("2 4 6 8"), 20)
        self.assertEqual(max_even_sum([10, 20, 30]), 60)

    # 5. Все элементы нечетные
    def test_all_odd(self):
        """Все элементы нечетные."""
        # Нечетное количество нечетных: исключаем минимальное (1) -> 3 + 5 = 8
        self.assertEqual(max_even_sum("1 3 5"), 8)
        # Четное количество нечетных: сумма уже четная -> 1 + 3 + 5 + 7 = 16
        self.assertEqual(max_even_sum("1 3 5 7"), 16)
        # Повторяющиеся нечетные элементы
        self.assertEqual(max_even_sum("3 3 3"), 6)
        self.assertEqual(max_even_sum("5 5"), 10)

    # 6. Смешанные массивы
    def test_mixed_arrays(self):
        """Массивы со смешанными четными и нечетными числами."""
        self.assertEqual(max_even_sum("2 4 3 5"), 14)
        self.assertEqual(max_even_sum("2 4 1 3 5"), 14)
        self.assertEqual(max_even_sum("10 20 7 1"), 38)
        self.assertEqual(max_even_sum("10 20 8 1"), 38)
        self.assertEqual(max_even_sum("10 20 7 3 5"), 42)

    # 7. Поддержка различных форматов входных данных
    def test_input_formats(self):
        """Проверка работы со строками с нестандартными пробелами и коллекциями."""
        # Множественные пробелы и переносы
        self.assertEqual(max_even_sum("   5   7 \t 13 \n 2   14  "), 36)
        # Кортежи и генераторы
        self.assertEqual(max_even_sum((5, 7, 13, 2, 14)), 36)
        self.assertEqual(max_even_sum(x for x in [5, 7, 13, 2, 14]), 36)

    # 8. Нетривиальные и большие значения
    def test_large_numbers(self):
        """Проверка работы с большими числами."""
        large_evens = [10**9, 2 * 10**9]
        self.assertEqual(max_even_sum(large_evens), 3 * 10**9)

        large_mixed = [10**9 + 1, 10**9 + 3, 10**9 + 5]  # сумма 3*10^9 + 9 (нечет)
        # min_odd = 10^9 + 1 -> сумма = 2*10^9 + 8
        self.assertEqual(max_even_sum(large_mixed), 2 * 10**9 + 8)

    # 9. Обработка ошибок ввода
    def test_invalid_values(self):
        """Проверка обработки некорректных значений и типов."""
        # Неположительные числа (0 и отрицательные)
        with self.assertRaises(ValueError):
            max_even_sum("0 2 4")
        with self.assertRaises(ValueError):
            max_even_sum("-5 7 13")
        with self.assertRaises(ValueError):
            max_even_sum([5, -2, 4])

        # Некорректный тип элементов
        with self.assertRaises(TypeError):
            max_even_sum([2, "abc", 4])
        with self.assertRaises(TypeError):
            max_even_sum([2, 3.5, 4])
        with self.assertRaises(TypeError):
            max_even_sum([True, 2, 4])
        with self.assertRaises(TypeError):
            max_even_sum(12345)


if __name__ == "__main__":
    unittest.main()

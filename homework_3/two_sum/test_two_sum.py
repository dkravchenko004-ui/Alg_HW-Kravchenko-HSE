"""Тесты для задачи 1: Two sum."""

import unittest
from homework_3.two_sum.solution import two_sum


class TestTwoSum(unittest.TestCase):
    """Набор тестов для функции two_sum."""

    def test_examples_from_description(self):
        """Примеры из условия."""
        self.assertEqual(two_sum([1, 3, 4, 10], 7), "1 2")
        self.assertEqual(two_sum([5, 5, 1, 4], 10), "0 1")

    def test_pair_at_edges(self):
        """Пара на краях массива."""
        self.assertEqual(two_sum([2, 7, 11, 15], 17), "0 3")
        self.assertEqual(two_sum([9, 1, 2, 3], 12), "0 3")

    def test_first_two_elements(self):
        """Сумма первых двух элементов."""
        self.assertEqual(two_sum([3, 4, 10], 7), "0 1")

    def test_last_two_elements(self):
        """Сумма последних двух элементов."""
        self.assertEqual(two_sum([10, 1, 2, 8], 10), "2 3")

    def test_negatives_and_zero(self):
        """Отрицательные числа и ноль."""
        self.assertEqual(two_sum([-3, 1, 4], 1), "0 2")
        self.assertEqual(two_sum([0, 5, -5, 2], 0), "1 2")
        self.assertEqual(two_sum([-1, -2, -3], -5), "1 2")

    def test_duplicate_values(self):
        """Одинаковые значения на разных индексах, один элемент дважды не берём."""
        self.assertEqual(two_sum([5, 5, 1, 4], 10), "0 1")
        self.assertEqual(two_sum([1, 8, 8, 2], 16), "1 2")

    def test_string_input(self):
        """Массив можно передать строкой через пробел."""
        self.assertEqual(two_sum("1 3 4 10", 7), "1 2")
        self.assertEqual(two_sum("  5   5  1  4 ", 10), "0 1")

    def test_indices_in_ascending_order(self):
        """В ответе меньший индекс всегда слева."""
        result = two_sum([4, 1, 6, 3], 9)
        left, right = result.split()
        self.assertLess(int(left), int(right))
        self.assertEqual(result, "2 3")

    def test_invalid_input(self):
        """Пустой массив, одно число, не те типы."""
        with self.assertRaises(ValueError):
            two_sum([], 1)
        with self.assertRaises(ValueError):
            two_sum([5], 5)
        with self.assertRaises(ValueError):
            two_sum("", 1)
        with self.assertRaises(TypeError):
            two_sum([1, 2, 3], 7.0)
        with self.assertRaises(TypeError):
            two_sum([1, True], 2)
        with self.assertRaises(TypeError):
            two_sum(123, 3)


if __name__ == "__main__":
    unittest.main()

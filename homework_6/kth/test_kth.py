"""Тесты для задачи 3: k-й по величине, quickselect."""

import unittest
from unittest.mock import patch

from homework_6.kth.solution import kth_largest


class TestKthLargest(unittest.TestCase):
    """Примеры из условия, границы, запрет полной сортировки."""

    def test_examples_from_statement(self):
        """Два примера с формулировки."""
        self.assertEqual(kth_largest([3, 2, 1, 5, 6, 4], 2), 5)
        self.assertEqual(kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)

    def test_k_one_is_maximum(self):
        self.assertEqual(kth_largest([3, 2, 1, 5, 6, 4], 1), 6)

    def test_k_n_is_minimum(self):
        self.assertEqual(kth_largest([3, 2, 1, 5, 6, 4], 6), 1)

    def test_single_element(self):
        self.assertEqual(kth_largest([9], 1), 9)

    def test_all_equal(self):
        self.assertEqual(kth_largest([4, 4, 4, 4], 2), 4)

    def test_negatives(self):
        self.assertEqual(kth_largest([-1, -7, 3, 0], 2), 0)

    def test_does_not_mutate_input(self):
        data = [3, 2, 1, 5, 6, 4]
        original = list(data)
        kth_largest(data, 2)
        self.assertEqual(data, original)

    def test_accepts_tuple(self):
        self.assertEqual(kth_largest((3, 2, 1, 5, 6, 4), 2), 5)

    def test_does_not_call_sorted(self):
        """По условию нельзя просто отсортировать массив."""
        with patch("builtins.sorted", side_effect=AssertionError("sorted запрещён")):
            self.assertEqual(kth_largest([3, 2, 1, 5, 6, 4], 2), 5)

    def test_matches_sorted_descending(self):
        """Совпадает с k-м элементом убывающего порядка (проверка в тесте)."""
        data = [7, 1, 4, 9, 2, 4, 8]
        for k in range(1, len(data) + 1):
            expect = sorted(data, reverse=True)[k - 1]
            self.assertEqual(kth_largest(data, k), expect)

    def test_k_out_of_range(self):
        with self.assertRaises(ValueError):
            kth_largest([1, 2, 3], 0)
        with self.assertRaises(ValueError):
            kth_largest([1, 2, 3], 4)
        with self.assertRaises(ValueError):
            kth_largest([], 1)

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            kth_largest("123", 1)
        with self.assertRaises(TypeError):
            kth_largest([1, 2], 1.0)
        with self.assertRaises(TypeError):
            kth_largest([1, True], 1)
        with self.assertRaises(TypeError):
            kth_largest([1, 2], True)


if __name__ == "__main__":
    unittest.main()

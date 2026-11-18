"""Тесты для задачи 2: итеративные mergesort и quicksort."""

import unittest

from homework_6.compare.solution import mergesort, quicksort
from homework_6.iterative.solution import mergesort_iterative, quicksort_iterative


class TestIterativeSorts(unittest.TestCase):
    """Итеративные версии совпадают с рекурсивными на тех же входах."""

    def test_small_unsorted(self):
        data = [5, 2, 8, 1, 3]
        self.assertEqual(mergesort_iterative(data), [1, 2, 3, 5, 8])
        self.assertEqual(quicksort_iterative(data), [1, 2, 3, 5, 8])

    def test_empty_and_single(self):
        self.assertEqual(mergesort_iterative([]), [])
        self.assertEqual(quicksort_iterative([]), [])
        self.assertEqual(mergesort_iterative([4]), [4])
        self.assertEqual(quicksort_iterative([4]), [4])

    def test_already_sorted(self):
        data = [1, 2, 3, 4, 5]
        self.assertEqual(mergesort_iterative(data), data)
        self.assertEqual(quicksort_iterative(data), data)

    def test_reversed(self):
        data = [9, 6, 3, 0]
        self.assertEqual(mergesort_iterative(data), [0, 3, 6, 9])
        self.assertEqual(quicksort_iterative(data), [0, 3, 6, 9])

    def test_duplicates_and_negatives(self):
        data = [2, -1, 2, 0, -1]
        self.assertEqual(mergesort_iterative(data), [-1, -1, 0, 2, 2])
        self.assertEqual(quicksort_iterative(data), [-1, -1, 0, 2, 2])

    def test_matches_recursive(self):
        """На одном наборе ответ как у рекурсивных из задачи 1."""
        data = [7, 1, 7, 3, 2, 9, 0, 4]
        self.assertEqual(mergesort_iterative(data), mergesort(data))
        self.assertEqual(quicksort_iterative(data), quicksort(data))

    def test_does_not_mutate_input(self):
        data = [4, 1, 3]
        original = list(data)
        mergesort_iterative(data)
        quicksort_iterative(data)
        self.assertEqual(data, original)

    def test_odd_length(self):
        """Нечётная длина: последний кусок при слиянии короче."""
        data = [4, 1, 5, 2, 3]
        self.assertEqual(mergesort_iterative(data), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort_iterative(data), [1, 2, 3, 4, 5])

    def test_large_sorted_no_recursion_limit(self):
        """Длинный возрастающий ряд: итеративный quicksort не упирается в стек."""
        data = list(range(2500))
        self.assertEqual(quicksort_iterative(data), data)
        self.assertEqual(mergesort_iterative(data[::-1]), data)

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            mergesort_iterative(None)
        with self.assertRaises(TypeError):
            quicksort_iterative("abc")
        with self.assertRaises(TypeError):
            mergesort_iterative([1, False])


if __name__ == "__main__":
    unittest.main()

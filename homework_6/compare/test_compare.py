"""Тесты для задачи 1: рекурсивные mergesort / quicksort и timed."""

import unittest

from homework_6.compare.solution import mergesort, quicksort, timed


class TestCompareSorts(unittest.TestCase):
    """Корректность сортировок и декоратор времени."""

    def test_small_unsorted(self):
        """Короткий неупорядоченный массив."""
        data = [5, 2, 8, 1, 3]
        self.assertEqual(mergesort(data), [1, 2, 3, 5, 8])
        self.assertEqual(quicksort(data), [1, 2, 3, 5, 8])

    def test_empty_and_single(self):
        """Пустой массив и один элемент."""
        self.assertEqual(mergesort([]), [])
        self.assertEqual(quicksort([]), [])
        self.assertEqual(mergesort([7]), [7])
        self.assertEqual(quicksort([7]), [7])

    def test_already_sorted(self):
        """Уже по возрастанию — mergesort не ломает, quicksort тоже."""
        data = [1, 2, 3, 4]
        self.assertEqual(mergesort(data), data)
        self.assertEqual(quicksort(data), data)

    def test_reversed(self):
        """Убывающий массив."""
        data = [9, 7, 4, 1]
        self.assertEqual(mergesort(data), [1, 4, 7, 9])
        self.assertEqual(quicksort(data), [1, 4, 7, 9])

    def test_duplicates(self):
        """Повторы остаются, порядок по значению."""
        data = [3, 1, 3, 2, 1]
        self.assertEqual(mergesort(data), [1, 1, 2, 3, 3])
        self.assertEqual(quicksort(data), [1, 1, 2, 3, 3])

    def test_all_equal(self):
        """Все элементы одинаковые."""
        data = [4, 4, 4, 4]
        self.assertEqual(mergesort(data), data)
        self.assertEqual(quicksort(data), data)

    def test_negatives(self):
        """Отрицательные и ноль."""
        data = [0, -2, 5, -2, 1]
        self.assertEqual(mergesort(data), [-2, -2, 0, 1, 5])
        self.assertEqual(quicksort(data), [-2, -2, 0, 1, 5])

    def test_does_not_mutate_input(self):
        """Исходный список не меняется."""
        data = [4, 1, 3]
        original = list(data)
        mergesort(data)
        quicksort(data)
        self.assertEqual(data, original)

    def test_accepts_tuple(self):
        """Последовательность, не только list."""
        self.assertEqual(mergesort((3, 1, 2)), [1, 2, 3])
        self.assertEqual(quicksort((3, 1, 2)), [1, 2, 3])

    def test_invalid_type(self):
        """Не последовательность или не целые — TypeError."""
        with self.assertRaises(TypeError):
            mergesort(123)
        with self.assertRaises(TypeError):
            quicksort("12")
        with self.assertRaises(TypeError):
            mergesort([1, 2.5])
        with self.assertRaises(TypeError):
            quicksort([1, True])

    def test_timed_records_duration(self):
        """После вызова last_time — неотрицательное число."""
        mergesort([3, 1, 2])
        self.assertIsInstance(mergesort.last_time, float)
        self.assertGreaterEqual(mergesort.last_time, 0.0)
        quicksort([3, 1, 2])
        self.assertGreaterEqual(quicksort.last_time, 0.0)

    def test_timed_keeps_result(self):
        """Декоратор не подменяет ответ функции."""

        @timed
        def add(a, b):
            return a + b

        self.assertEqual(add(2, 3), 5)
        self.assertGreaterEqual(add.last_time, 0.0)

    def test_sorted_input_quicksort_slower(self):
        """Опорный — последний: на возрастающем массиве quicksort заметно дольше.

        Mergesort всегда ~ n log n. Quicksort здесь вырождается в n^2.
        """
        data = list(range(500))
        mergesort(data)
        t_merge = mergesort.last_time
        quicksort(data)
        t_quick = quicksort.last_time
        self.assertGreater(
            t_quick,
            t_merge * 2,
            f"ожидали quicksort >> mergesort, qs={t_quick:.6f}s ms={t_merge:.6f}s",
        )


if __name__ == "__main__":
    unittest.main()

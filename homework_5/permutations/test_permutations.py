"""Тесты для задачи 2: перестановки."""

import io
import unittest
from contextlib import redirect_stdout

from homework_5.permutations.solution import permute
from homework_5.tracer.solution import trace


class TestPermutations(unittest.TestCase):
    """Набор тестов для permute."""

    def setUp(self):
        trace.depth = 0

    def _run(self, nums):
        with redirect_stdout(io.StringIO()):
            return permute(nums)

    def test_examples_from_description(self):
        """Примеры из условия."""
        self.assertEqual(
            self._run([1, 2, 3]),
            [
                [1, 2, 3],
                [1, 3, 2],
                [2, 1, 3],
                [2, 3, 1],
                [3, 1, 2],
                [3, 2, 1],
            ],
        )
        self.assertEqual(self._run([0, 1]), [[0, 1], [1, 0]])
        self.assertEqual(self._run([1]), [[1]])

    def test_empty(self):
        """Пустой массив: одна пустая перестановка."""
        self.assertEqual(self._run([]), [[]])

    def test_two_elements(self):
        """Два элемента — две перестановки."""
        self.assertEqual(self._run([4, 5]), [[4, 5], [5, 4]])

    def test_count_is_factorial(self):
        """Число перестановок равно n!."""
        self.assertEqual(len(self._run([1, 2, 3, 4])), 24)

    def test_all_unique_and_complete(self):
        """Нет дубликатов, каждый индекс использован по разу."""
        result = self._run([1, 2, 3])
        as_tuples = [tuple(item) for item in result]
        self.assertEqual(len(as_tuples), len(set(as_tuples)))
        for item in result:
            self.assertEqual(sorted(item), [1, 2, 3])

    def test_trace_shows_stack(self):
        """Декоратор из задачи 1 печатает вход, отступ и возврат."""
        buf = io.StringIO()
        with redirect_stdout(buf):
            permute([1, 2])
        text = buf.getvalue()
        self.assertIn("-> generate([])", text)
        self.assertIn("  -> generate([1])", text)
        self.assertIn("    -> generate([1, 2])", text)
        self.assertIn("    <- generate([1, 2]) = [[1, 2]]", text)
        self.assertIn("<- generate([]) = [[1, 2], [2, 1]]", text)

    def test_invalid_input(self):
        """Не последовательность — TypeError."""
        with self.assertRaises(TypeError):
            self._run(123)
        with self.assertRaises(TypeError):
            self._run("12")


if __name__ == "__main__":
    unittest.main()

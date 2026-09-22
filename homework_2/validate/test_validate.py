"""Тесты для задачи 2: проверка последовательности push/pop."""

import unittest
from homework_2.validate.solution import validate


class TestValidate(unittest.TestCase):
    """Набор тестов для функции validate."""

    def test_examples_from_description(self):
        """Примеры из условия."""
        self.assertTrue(validate("1 2 3 4 5", "1 3 5 4 2"))
        self.assertTrue(validate([1, 2, 3, 4, 5], [1, 3, 5, 4, 2]))
        self.assertFalse(validate("1 2 3", "3 1 2"))
        self.assertFalse(validate([1, 2, 3], [3, 1, 2]))

    def test_single_element(self):
        """Граница: один элемент."""
        self.assertTrue(validate([7], [7]))
        self.assertTrue(validate("42", "42"))

    def test_push_all_then_pop_all(self):
        """Сначала все push, потом все pop — popped это pushed наоборот."""
        self.assertTrue(validate([1, 2, 3, 4], [4, 3, 2, 1]))
        self.assertTrue(validate([1, 2, 3], [3, 2, 1]))

    def test_pop_right_after_push(self):
        """После каждого push сразу pop — последовательности совпадают."""
        self.assertTrue(validate([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))
        self.assertTrue(validate("9 8 7", "9 8 7"))

    def test_mixed_valid(self):
        """Допустимые чередования push и pop."""
        self.assertTrue(validate([1, 2, 3], [2, 3, 1]))
        self.assertTrue(validate([1, 2, 3], [2, 1, 3]))
        self.assertTrue(validate([1, 2, 3, 4, 5], [1, 2, 3, 5, 4]))
        self.assertTrue(validate([1, 2, 3, 4, 5], [2, 1, 3, 5, 4]))
        self.assertTrue(validate([1, 2, 3, 4, 5], [3, 2, 1, 4, 5]))

    def test_invalid_sequences(self):
        """Нужный элемент не на вершине — последовательность невозможна."""
        self.assertFalse(validate([1, 2, 3], [3, 1, 2]))
        self.assertFalse(validate([1, 2, 3, 4], [3, 1, 4, 2]))
        self.assertFalse(validate([1, 2, 3, 4], [4, 2, 3, 1]))
        self.assertFalse(validate([1, 2, 3, 4, 5], [4, 5, 3, 1, 2]))
        self.assertFalse(validate([1, 2, 3, 4, 5], [3, 5, 4, 1, 2]))

    def test_input_formats(self):
        """Строка с пробелами, кортеж, генератор."""
        self.assertTrue(validate("  1   2  3  ", "  1  2  3 "))
        self.assertTrue(validate((1, 2, 3, 4, 5), (1, 3, 5, 4, 2)))
        self.assertTrue(
            validate(
                (x for x in [1, 2, 3, 4, 5]),
                (x for x in [1, 3, 5, 4, 2]),
            )
        )

    def test_large_n(self):
        """Верхняя граница n = 100000."""
        n = 100000
        pushed = list(range(n))
        popped_reversed = list(range(n - 1, -1, -1))
        self.assertTrue(validate(pushed, popped_reversed))
        self.assertTrue(validate(pushed, pushed))

        bad = list(range(n - 1, -1, -1))
        bad[-2], bad[-1] = bad[-1], bad[-2]
        self.assertFalse(validate(pushed, bad))

    def test_invalid_input(self):
        """Пустой ввод, разная длина, некорректные типы."""
        with self.assertRaises(ValueError):
            validate([], [])
        with self.assertRaises(ValueError):
            validate("", "1")
        with self.assertRaises(ValueError):
            validate([1, 2], [1])
        with self.assertRaises(ValueError):
            validate("1 2 a", "1 2 3")
        with self.assertRaises(TypeError):
            validate([1, True], [1, True])
        with self.assertRaises(TypeError):
            validate([1, 2.0], [1, 2])
        with self.assertRaises(TypeError):
            validate(123, [1, 2, 3])


if __name__ == "__main__":
    unittest.main()

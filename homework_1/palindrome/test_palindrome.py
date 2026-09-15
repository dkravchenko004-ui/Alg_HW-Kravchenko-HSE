"""Тесты для задачи 1: Палиндром (без использования строк)."""

import unittest
from homework_1.palindrome.solution import is_palindrome


class TestIsPalindrome(unittest.TestCase):
    """Набор тестов для проверки функции is_palindrome."""

    def test_examples_from_description(self):
        """Проверка примеров, указанных в условии."""
        self.assertTrue(is_palindrome(121), "121 должно быть True")
        self.assertFalse(is_palindrome(31), "31 должно быть False")

    def test_single_digit_numbers(self):
        """Любое однозначное положительное число является палиндромом."""
        for num in range(1, 10):
            with self.subTest(num=num):
                self.assertTrue(is_palindrome(num))

    def test_even_length_palindromes(self):
        """Палиндромы четной длины."""
        self.assertTrue(is_palindrome(11))
        self.assertTrue(is_palindrome(22))
        self.assertTrue(is_palindrome(1221))
        self.assertTrue(is_palindrome(133331))
        self.assertTrue(is_palindrome(12344321))

    def test_odd_length_palindromes(self):
        """Палиндромы нечетной длины."""
        self.assertTrue(is_palindrome(101))
        self.assertTrue(is_palindrome(505))
        self.assertTrue(is_palindrome(12321))
        self.assertTrue(is_palindrome(9876789))

    def test_non_palindromes(self):
        """Числа, не являющиеся палиндромами."""
        self.assertFalse(is_palindrome(12))
        self.assertFalse(is_palindrome(123))
        self.assertFalse(is_palindrome(1234))
        self.assertFalse(is_palindrome(1234320))
        self.assertFalse(is_palindrome(987654321))

    def test_multiples_of_ten(self):
        """Числа, заканчивающиеся на 0, не могут быть палиндромами."""
        self.assertFalse(is_palindrome(10))
        self.assertFalse(is_palindrome(20))
        self.assertFalse(is_palindrome(100))
        self.assertFalse(is_palindrome(1000))
        self.assertFalse(is_palindrome(1230))

    def test_palindromes_with_internal_zeros(self):
        """Палиндромы с нулями в середине."""
        self.assertTrue(is_palindrome(1001))
        self.assertTrue(is_palindrome(10001))
        self.assertTrue(is_palindrome(10201))
        self.assertTrue(is_palindrome(7000007))

    def test_non_positive_numbers(self):
        """По условию число целое положительное (n > 0)."""
        self.assertFalse(is_palindrome(0))
        self.assertFalse(is_palindrome(-1))
        self.assertFalse(is_palindrome(-121))
        self.assertFalse(is_palindrome(-1221))

    def test_large_numbers(self):
        """Большие числа (проверка на отсутствие переполнения и точность)."""
        large_palindrome = 1234567890987654321
        self.assertTrue(is_palindrome(large_palindrome))

        large_non_palindrome = 1234567890887654321
        self.assertFalse(is_palindrome(large_non_palindrome))

        almost_palindrome = 9234567890987654321
        self.assertFalse(is_palindrome(almost_palindrome))

    def test_type_errors(self):
        """Проверка обработки некорректных типов данных."""
        with self.assertRaises(TypeError):
            is_palindrome("121")
        with self.assertRaises(TypeError):
            is_palindrome(12.1)
        with self.assertRaises(TypeError):
            is_palindrome(True)
        with self.assertRaises(TypeError):
            is_palindrome(None)
        with self.assertRaises(TypeError):
            is_palindrome([1, 2, 1])


if __name__ == "__main__":
    unittest.main()

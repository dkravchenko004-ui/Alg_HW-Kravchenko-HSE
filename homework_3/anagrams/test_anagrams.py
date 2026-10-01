"""Тесты для задачи 2: группировка анаграмм."""

import unittest
from homework_3.anagrams.solution import group_anagrams


def _sorted_groups(groups):
    return sorted(tuple(sorted(group)) for group in groups)


class TestGroupAnagrams(unittest.TestCase):
    """Набор тестов для функции group_anagrams."""

    def test_example_from_description(self):
        """Пример из условия. Порядок групп в тесте не фиксируем."""
        result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        self.assertEqual(_sorted_groups(result), _sorted_groups(expected))

    def test_example_preserves_order(self):
        """Группы идут в порядке первого вхождения, слова — как во входе."""
        result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        self.assertEqual(
            result,
            [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
        )

    def test_empty_and_single(self):
        """Пустой список и одно слово."""
        self.assertEqual(group_anagrams([]), [])
        self.assertEqual(group_anagrams(["abc"]), [["abc"]])

    def test_no_anagrams(self):
        """Все слова разные, каждая группа из одного слова."""
        result = group_anagrams(["ab", "cd", "ef"])
        self.assertEqual(result, [["ab"], ["cd"], ["ef"]])

    def test_all_anagrams(self):
        """Все слова — анаграммы одного набора букв."""
        result = group_anagrams(["abc", "cab", "bca"])
        self.assertEqual(result, [["abc", "cab", "bca"]])

    def test_empty_strings(self):
        """Пустые строки — анаграммы друг друга."""
        result = group_anagrams(["", "", "a"])
        self.assertEqual(result, [["", ""], ["a"]])

    def test_single_letters(self):
        """Однобуквенные слова."""
        result = group_anagrams(["a", "b", "a"])
        self.assertEqual(result, [["a", "a"], ["b"]])

    def test_different_lengths(self):
        """Разная длина — точно не анаграммы."""
        result = group_anagrams(["ab", "ba", "abc"])
        self.assertEqual(result, [["ab", "ba"], ["abc"]])

    def test_string_input(self):
        """Слова через пробел в одной строке."""
        result = group_anagrams("eat tea tan")
        self.assertEqual(result, [["eat", "tea"], ["tan"]])

    def test_invalid_input(self):
        """Не строки в списке."""
        with self.assertRaises(TypeError):
            group_anagrams(["eat", 123])
        with self.assertRaises(TypeError):
            group_anagrams(123)


if __name__ == "__main__":
    unittest.main()

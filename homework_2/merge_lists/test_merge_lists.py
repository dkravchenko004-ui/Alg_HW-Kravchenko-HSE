"""Тесты для задачи 3: слияние двух отсортированных односвязных списков."""

import unittest
from homework_2.merge_lists.solution import (
    ListNode,
    from_list,
    merge_two_lists_dummy,
    merge_two_lists_no_dummy,
    to_list,
)


class TestMergeLists(unittest.TestCase):
    """Набор тестов для обоих способов слияния."""

    def _check(self, left, right, expected):
        dummy = to_list(merge_two_lists_dummy(from_list(left), from_list(right)))
        plain = to_list(merge_two_lists_no_dummy(from_list(left), from_list(right)))
        self.assertEqual(dummy, expected)
        self.assertEqual(plain, expected)

    def test_example_from_description(self):
        """Пример из условия."""
        self._check([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4])

    def test_both_empty(self):
        """Оба списка пустые."""
        self.assertIsNone(merge_two_lists_dummy(None, None))
        self.assertIsNone(merge_two_lists_no_dummy(None, None))
        self._check([], [], [])

    def test_one_empty(self):
        """Один список пустой — остаётся второй."""
        self._check([], [1, 2, 3], [1, 2, 3])
        self._check([4, 5], [], [4, 5])
        self._check([], [0], [0])

    def test_single_nodes(self):
        """Списки из одного узла."""
        self._check([1], [2], [1, 2])
        self._check([2], [1], [1, 2])
        self._check([3], [3], [3, 3])

    def test_already_ordered_halves(self):
        """Все элементы одного списка меньше элементов другого."""
        self._check([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6])
        self._check([10, 20], [1, 2, 3], [1, 2, 3, 10, 20])

    def test_duplicates(self):
        """Повторяющиеся значения."""
        self._check([1, 1, 2], [1, 3, 3], [1, 1, 1, 2, 3, 3])

    def test_negatives_and_zero(self):
        """Отрицательные числа и ноль."""
        self._check([-5, -1, 0], [-3, 2, 4], [-5, -3, -1, 0, 2, 4])

    def test_different_lengths(self):
        """Списки разной длины."""
        self._check([1, 8], [2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7, 8])

    def test_interleaved(self):
        """Узлы по очереди берутся из обоих списков."""
        self._check(
            [1, 3, 5, 7, 9],
            [2, 4, 6, 8, 10],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        )

    def test_reuses_original_nodes(self):
        """Результат собран из исходных узлов, а не из копий."""
        for merge in (merge_two_lists_dummy, merge_two_lists_no_dummy):
            left = from_list([1, 4, 6])
            right = from_list([2, 3, 5])
            original = set()
            for head in (left, right):
                cur = head
                while cur is not None:
                    original.add(id(cur))
                    cur = cur.next
            merged = merge(left, right)
            result_ids = set()
            cur = merged
            while cur is not None:
                result_ids.add(id(cur))
                cur = cur.next
            self.assertEqual(result_ids, original)
            self.assertEqual(to_list(merged), [1, 2, 3, 4, 5, 6])

    def test_dummy_is_not_in_result(self):
        """Фиктивный узел не попадает в ответ."""
        left = ListNode(1)
        right = ListNode(2)
        result = merge_two_lists_dummy(left, right)
        self.assertIs(result, left)
        self.assertIs(result.next, right)

    def test_no_dummy_head_is_smaller_node(self):
        """Без dummy голова — меньший из исходных узлов."""
        left = ListNode(5, ListNode(6))
        right = ListNode(1, ListNode(8))
        result = merge_two_lists_no_dummy(left, right)
        self.assertIs(result, right)
        self.assertEqual(to_list(result), [1, 5, 6, 8])

    def test_helpers(self):
        """from_list / to_list и проверка типов."""
        self.assertEqual(to_list(from_list([1, 2, 3, 4])), [1, 2, 3, 4])
        self.assertIsNone(from_list([]))
        self.assertEqual(to_list(None), [])
        with self.assertRaises(TypeError):
            from_list([1, "a"])
        with self.assertRaises(TypeError):
            from_list([True])


if __name__ == "__main__":
    unittest.main()

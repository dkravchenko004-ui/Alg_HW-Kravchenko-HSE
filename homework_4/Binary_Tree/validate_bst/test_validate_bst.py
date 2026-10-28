"""Тесты для задачи 2: проверка BST."""

import unittest
from homework_4.Binary_Tree.validate_bst.solution import TreeNode, is_valid_bst


class TestValidateBST(unittest.TestCase):
    """Набор тестов для is_valid_bst."""

    def test_empty_and_single(self):
        """Пустое дерево и один узел — корректные BST."""
        self.assertTrue(is_valid_bst(None))
        self.assertTrue(is_valid_bst(TreeNode(4)))

    def test_valid_small(self):
        """Обычное корректное дерево: 8, слева 3, справа 10."""
        root = TreeNode(8, TreeNode(3), TreeNode(10))
        self.assertTrue(is_valid_bst(root))

    def test_valid_deeper(self):
        """То же дерево, что в задаче 1: 8 / 3,10 / 1,6,14 / 4,7."""
        root = TreeNode(
            8,
            TreeNode(3, TreeNode(1), TreeNode(6, TreeNode(4), TreeNode(7))),
            TreeNode(10, None, TreeNode(14)),
        )
        self.assertTrue(is_valid_bst(root))

    def test_invalid_right_child_too_small(self):
        """Правый ребёнок меньше родителя."""
        root = TreeNode(5, TreeNode(3), TreeNode(4))
        self.assertFalse(is_valid_bst(root))

    def test_invalid_left_child_too_big(self):
        """Левый ребёнок больше родителя."""
        root = TreeNode(5, TreeNode(6), TreeNode(8))
        self.assertFalse(is_valid_bst(root))

    def test_invalid_deep_violation(self):
        """Локально дети ок, но 6 сидит слева от 5."""
        root = TreeNode(5, TreeNode(3, None, TreeNode(6)), TreeNode(7))
        self.assertFalse(is_valid_bst(root))

    def test_duplicates_on_right_ok(self):
        """Равные ключи справа допустимы — как при нашей вставке."""
        root = TreeNode(5, None, TreeNode(5))
        self.assertTrue(is_valid_bst(root))

    def test_duplicates_on_left_not_ok(self):
        """Равный ключ слева ломает правило «слева строго меньше»."""
        root = TreeNode(5, TreeNode(5), None)
        self.assertFalse(is_valid_bst(root))

    def test_sorted_chain_right(self):
        """Цепочка вправо 1-2-3 — валидный BST."""
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        self.assertTrue(is_valid_bst(root))

    def test_negatives(self):
        """Отрицательные ключи."""
        root = TreeNode(0, TreeNode(-2, TreeNode(-5)), TreeNode(4))
        self.assertTrue(is_valid_bst(root))
        bad = TreeNode(0, TreeNode(-2, None, TreeNode(1)), TreeNode(4))
        self.assertFalse(is_valid_bst(bad))

    def test_invalid_input(self):
        """Не узел дерева — TypeError."""
        with self.assertRaises(TypeError):
            is_valid_bst(5)
        with self.assertRaises(TypeError):
            is_valid_bst("tree")
        with self.assertRaises(TypeError):
            is_valid_bst(TreeNode(True))


if __name__ == "__main__":
    unittest.main()

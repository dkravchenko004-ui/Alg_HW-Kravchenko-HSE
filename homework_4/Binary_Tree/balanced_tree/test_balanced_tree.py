"""Тесты для задачи 3: баланс по высоте."""

import unittest
from homework_4.Binary_Tree.balanced_tree.solution import TreeNode, is_balanced


class TestBalancedTree(unittest.TestCase):
    """Набор тестов для is_balanced."""

    def test_empty_and_single(self):
        """Пустое дерево и один узел сбалансированы."""
        self.assertTrue(is_balanced(None))
        self.assertTrue(is_balanced(TreeNode(1)))

    def test_two_nodes(self):
        """Корень и один ребёнок: высоты 1 и 0, разница 1 — ок."""
        self.assertTrue(is_balanced(TreeNode(1, TreeNode(2))))
        self.assertTrue(is_balanced(TreeNode(1, None, TreeNode(2))))

    def test_perfect_small(self):
        """Полное дерево высоты 2."""
        root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
        self.assertTrue(is_balanced(root))

    def test_height_diff_one(self):
        """Левая высота 2, правая 1 — ещё допустимо."""
        root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
        self.assertTrue(is_balanced(root))

    def test_chain_unbalanced(self):
        """Цепочка 1-2-3-4: у корня разница высот больше 1."""
        root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
        self.assertFalse(is_balanced(root))

    def test_subtrees_ok_root_not(self):
        """Оба поддерева сбалансированы, корень — нет."""
        # слева высота 3, справа 1
        root = TreeNode(
            1,
            TreeNode(2, TreeNode(4, TreeNode(6)), TreeNode(5)),
            TreeNode(3),
        )
        self.assertFalse(is_balanced(root))

    def test_right_heavy(self):
        """Перекос вправо."""
        root = TreeNode(1, TreeNode(2), TreeNode(3, None, TreeNode(4, None, TreeNode(5))))
        self.assertFalse(is_balanced(root))

    def test_bst_example_from_task_one(self):
        """Дерево 8 / 3,10 / 1,6,14 / 4,7 сбалансировано."""
        root = TreeNode(
            8,
            TreeNode(3, TreeNode(1), TreeNode(6, TreeNode(4), TreeNode(7))),
            TreeNode(10, None, TreeNode(14)),
        )
        self.assertTrue(is_balanced(root))

    def test_only_left_grandchild_ok(self):
        """Как в условии: разница 1 у каждого узла."""
        root = TreeNode(10, TreeNode(5, TreeNode(1)), TreeNode(20))
        self.assertTrue(is_balanced(root))

    def test_invalid_input(self):
        """Не узел дерева — TypeError."""
        with self.assertRaises(TypeError):
            is_balanced(1)
        with self.assertRaises(TypeError):
            is_balanced("tree")
        with self.assertRaises(TypeError):
            is_balanced([1, 2, 3])


if __name__ == "__main__":
    unittest.main()

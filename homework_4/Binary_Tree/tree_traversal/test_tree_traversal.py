"""Тесты для задачи 1: BST и шесть обходов."""

import unittest
from homework_4.Binary_Tree.tree_traversal.solution import BST


def _fill(values):
    tree = BST()
    for value in values:
        tree.insert(value)
    return tree


class TestTreeTraversal(unittest.TestCase):
    """Набор тестов для BST и обходов."""

    def test_empty_tree(self):
        """Пустое дерево: все обходы дают пустой список."""
        tree = BST()
        self.assertEqual(tree.preorder(), [])
        self.assertEqual(tree.inorder(), [])
        self.assertEqual(tree.postorder(), [])
        self.assertEqual(tree.reverse_preorder(), [])
        self.assertEqual(tree.reverse_inorder(), [])
        self.assertEqual(tree.reverse_postorder(), [])

    def test_single_node(self):
        """Один узел: любой обход — само значение."""
        tree = _fill([7])
        self.assertEqual(tree.preorder(), [7])
        self.assertEqual(tree.inorder(), [7])
        self.assertEqual(tree.postorder(), [7])
        self.assertEqual(tree.reverse_preorder(), [7])
        self.assertEqual(tree.reverse_inorder(), [7])
        self.assertEqual(tree.reverse_postorder(), [7])

    def test_example_tree_all_traversals(self):
        """Нетривиальное дерево из README: 8, 3, 10, 1, 6, 14, 4, 7."""
        tree = _fill([8, 3, 10, 1, 6, 14, 4, 7])
        self.assertEqual(tree.preorder(), [8, 3, 1, 6, 4, 7, 10, 14])
        self.assertEqual(tree.inorder(), [1, 3, 4, 6, 7, 8, 10, 14])
        self.assertEqual(tree.postorder(), [1, 4, 7, 6, 3, 14, 10, 8])
        self.assertEqual(tree.reverse_preorder(), [8, 10, 14, 3, 6, 7, 4, 1])
        self.assertEqual(tree.reverse_inorder(), [14, 10, 8, 7, 6, 4, 3, 1])
        self.assertEqual(tree.reverse_postorder(), [14, 10, 7, 4, 6, 1, 3, 8])

    def test_inorder_is_sorted(self):
        """Inorder BST даёт значения по возрастанию."""
        values = [5, 2, 8, 1, 3, 7, 9]
        tree = _fill(values)
        self.assertEqual(tree.inorder(), sorted(values))

    def test_reverse_inorder_is_descending(self):
        """Reverse inorder BST даёт значения по убыванию."""
        values = [5, 2, 8, 1, 3, 7, 9]
        tree = _fill(values)
        self.assertEqual(tree.reverse_inorder(), sorted(values, reverse=True))

    def test_left_skewed(self):
        """Вырожденное дерево влево: 3, 2, 1."""
        tree = _fill([3, 2, 1])
        self.assertEqual(tree.preorder(), [3, 2, 1])
        self.assertEqual(tree.inorder(), [1, 2, 3])
        self.assertEqual(tree.postorder(), [1, 2, 3])
        self.assertEqual(tree.reverse_preorder(), [3, 2, 1])
        self.assertEqual(tree.reverse_inorder(), [3, 2, 1])
        self.assertEqual(tree.reverse_postorder(), [1, 2, 3])

    def test_right_skewed(self):
        """Вырожденное дерево вправо: 1, 2, 3."""
        tree = _fill([1, 2, 3])
        self.assertEqual(tree.preorder(), [1, 2, 3])
        self.assertEqual(tree.inorder(), [1, 2, 3])
        self.assertEqual(tree.postorder(), [3, 2, 1])
        self.assertEqual(tree.reverse_preorder(), [1, 2, 3])
        self.assertEqual(tree.reverse_inorder(), [3, 2, 1])
        self.assertEqual(tree.reverse_postorder(), [3, 2, 1])

    def test_duplicates_go_right(self):
        """Одинаковые ключи идут вправо, inorder не убывает."""
        tree = _fill([5, 5, 5])
        self.assertEqual(tree.inorder(), [5, 5, 5])
        self.assertEqual(tree.preorder(), [5, 5, 5])
        self.assertIsNone(tree.root.left)
        self.assertEqual(tree.root.right.value, 5)

    def test_negative_and_zero(self):
        """Отрицательные числа и ноль."""
        tree = _fill([0, -2, 3, -5])
        self.assertEqual(tree.inorder(), [-5, -2, 0, 3])

    def test_insert_keeps_bst_links(self):
        """После вставки 8, 3, 10 левый ребёнок 8 — тройка, правый — десять."""
        tree = _fill([8, 3, 10])
        self.assertEqual(tree.root.value, 8)
        self.assertEqual(tree.root.left.value, 3)
        self.assertEqual(tree.root.right.value, 10)

    def test_invalid_insert(self):
        """Нецелое значение — TypeError."""
        tree = BST()
        with self.assertRaises(TypeError):
            tree.insert(1.5)
        with self.assertRaises(TypeError):
            tree.insert(True)
        with self.assertRaises(TypeError):
            tree.insert("8")


if __name__ == "__main__":
    unittest.main()

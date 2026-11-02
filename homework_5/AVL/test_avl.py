"""Тесты для задачи 3: АВЛ-дерево."""

import unittest
from homework_5.AVL.solution import AVL


def _height(node):
    return 0 if node is None else node.height


def _assert_avl(test, node, low=None, high=None):
    if node is None:
        return 0
    if low is not None:
        test.assertGreater(node.key, low)
    if high is not None:
        test.assertLess(node.key, high)
    left_h = _assert_avl(test, node.left, low, node.key)
    right_h = _assert_avl(test, node.right, node.key, high)
    test.assertEqual(node.height, 1 + max(left_h, right_h))
    test.assertLessEqual(abs(left_h - right_h), 1)
    return node.height


class TestAVL(unittest.TestCase):
    """Набор тестов для AVL."""

    def test_empty_search(self):
        """Пустое дерево: поиска нет."""
        tree = AVL()
        self.assertFalse(tree.search(1))
        self.assertEqual(tree.inorder(), [])

    def test_insert_and_search(self):
        """Вставка нескольких ключей, поиск существующих и нет."""
        tree = AVL()
        for key in [5, 2, 8]:
            tree.insert(key)
        self.assertTrue(tree.search(5))
        self.assertTrue(tree.search(2))
        self.assertFalse(tree.search(7))
        self.assertEqual(tree.inorder(), [2, 5, 8])
        _assert_avl(self, tree.root)

    def test_duplicate_insert_ignored(self):
        """Повторная вставка того же ключа не меняет дерево."""
        tree = AVL()
        tree.insert(4)
        tree.insert(4)
        self.assertEqual(tree.inorder(), [4])
        self.assertIsNone(tree.root.left)
        self.assertIsNone(tree.root.right)

    def test_rr_rotation(self):
        """Вставка 10, 20, 30 — левый поворот вокруг 10."""
        tree = AVL()
        tree.insert(10)
        tree.insert(20)
        tree.insert(30)
        self.assertEqual(tree.root.key, 20)
        self.assertEqual(tree.root.left.key, 10)
        self.assertEqual(tree.root.right.key, 30)
        self.assertEqual(tree.inorder(), [10, 20, 30])
        _assert_avl(self, tree.root)

    def test_ll_rotation(self):
        """Вставка 30, 20, 10 — правый поворот вокруг 30."""
        tree = AVL()
        tree.insert(30)
        tree.insert(20)
        tree.insert(10)
        self.assertEqual(tree.root.key, 20)
        self.assertEqual(tree.root.left.key, 10)
        self.assertEqual(tree.root.right.key, 30)
        _assert_avl(self, tree.root)

    def test_lr_rotation(self):
        """Вставка 30, 10, 20 — большой правый поворот."""
        tree = AVL()
        tree.insert(30)
        tree.insert(10)
        tree.insert(20)
        self.assertEqual(tree.root.key, 20)
        self.assertEqual(tree.root.left.key, 10)
        self.assertEqual(tree.root.right.key, 30)
        _assert_avl(self, tree.root)

    def test_rl_rotation(self):
        """Вставка 10, 30, 20 — большой левый поворот."""
        tree = AVL()
        tree.insert(10)
        tree.insert(30)
        tree.insert(20)
        self.assertEqual(tree.root.key, 20)
        self.assertEqual(tree.root.left.key, 10)
        self.assertEqual(tree.root.right.key, 30)
        _assert_avl(self, tree.root)

    def test_many_inserts_stay_balanced(self):
        """Последовательность 1..20 не вытягивается в цепочку."""
        tree = AVL()
        for key in range(1, 21):
            tree.insert(key)
            _assert_avl(self, tree.root)
        self.assertEqual(tree.inorder(), list(range(1, 21)))
        self.assertLessEqual(_height(tree.root), 6)

    def test_delete_leaf(self):
        """Удаление листа."""
        tree = AVL()
        for key in [2, 1, 3]:
            tree.insert(key)
        tree.delete(1)
        self.assertFalse(tree.search(1))
        self.assertEqual(tree.inorder(), [2, 3])
        _assert_avl(self, tree.root)

    def test_delete_one_child(self):
        """Удаление узла с одним ребёнком."""
        tree = AVL()
        for key in [2, 1, 3, 4]:
            tree.insert(key)
        tree.delete(3)
        self.assertFalse(tree.search(3))
        self.assertTrue(tree.search(4))
        self.assertEqual(tree.inorder(), [1, 2, 4])
        _assert_avl(self, tree.root)

    def test_delete_two_children(self):
        """Удаление узла с двумя детьми: на место встаёт преемник."""
        tree = AVL()
        for key in [20, 10, 30, 25, 40]:
            tree.insert(key)
        tree.delete(20)
        self.assertFalse(tree.search(20))
        self.assertEqual(tree.inorder(), [10, 25, 30, 40])
        _assert_avl(self, tree.root)

    def test_delete_rebalances(self):
        """После удаления дерево снова с балансом |bf| <= 1."""
        tree = AVL()
        for key in [10, 20, 30, 40, 50, 25]:
            tree.insert(key)
        tree.delete(10)
        _assert_avl(self, tree.root)
        self.assertEqual(tree.inorder(), [20, 25, 30, 40, 50])

    def test_delete_missing_key(self):
        """Нет ключа — KeyError."""
        tree = AVL()
        tree.insert(1)
        with self.assertRaises(KeyError):
            tree.delete(9)
        with self.assertRaises(KeyError):
            AVL().delete(1)

    def test_delete_last_node(self):
        """Удаление единственного ключа оставляет пустое дерево."""
        tree = AVL()
        tree.insert(7)
        tree.delete(7)
        self.assertIsNone(tree.root)
        self.assertEqual(tree.inorder(), [])

    def test_invalid_key(self):
        """Нецелое — TypeError."""
        tree = AVL()
        with self.assertRaises(TypeError):
            tree.insert(1.5)
        with self.assertRaises(TypeError):
            tree.search(True)
        with self.assertRaises(TypeError):
            tree.delete("a")


if __name__ == "__main__":
    unittest.main()

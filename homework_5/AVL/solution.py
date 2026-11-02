"""Задача 3. АВЛ-дерево: вставка, удаление, поиск.

Подробное объяснение, сложность и визуализация:
см. README.md
"""

from typing import List, Optional


class AVLNode:
    """Узел АВЛ-дерева. height — высота поддерева с этим корнем."""

    def __init__(self, key: int) -> None:
        self.key = key
        self.left: Optional["AVLNode"] = None
        self.right: Optional["AVLNode"] = None
        self.height = 1


def _require_int(value: object) -> int:
    if not isinstance(value, int) or isinstance(value, bool):
        raise TypeError(
            f"ожидалось целое число, получено: {type(value).__name__}"
        )
    return value


class AVL:
    """Сбалансированное по высоте дерево поиска."""

    def __init__(self) -> None:
        self.root: Optional[AVLNode] = None

    def insert(self, key: int) -> None:
        """Вставляет ключ. Дубликат не добавляется повторно."""
        key = _require_int(key)
        self.root = self._insert(self.root, key)

    def delete(self, key: int) -> None:
        """Удаляет ключ. Нет ключа — KeyError."""
        key = _require_int(key)
        if not self.search(key):
            raise KeyError(key)
        self.root = self._delete(self.root, key)

    def search(self, key: int) -> bool:
        """True, если ключ есть в дереве."""
        key = _require_int(key)
        node = self.root
        while node is not None:
            if key == node.key:
                return True
            if key < node.key:
                node = node.left
            else:
                node = node.right
        return False

    def inorder(self) -> List[int]:
        """Ключи по возрастанию."""
        out: List[int] = []
        self._inorder(self.root, out)
        return out

    def _inorder(self, node: Optional[AVLNode], out: List[int]) -> None:
        if node is None:
            return
        self._inorder(node.left, out)
        out.append(node.key)
        self._inorder(node.right, out)

    def _height(self, node: Optional[AVLNode]) -> int:
        return 0 if node is None else node.height

    def _update(self, node: AVLNode) -> None:
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _bf(self, node: Optional[AVLNode]) -> int:
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _left_rotate(self, x: AVLNode) -> AVLNode:
        y = x.right
        assert y is not None
        tail = y.left
        y.left = x
        x.right = tail
        self._update(x)
        self._update(y)
        return y

    def _right_rotate(self, y: AVLNode) -> AVLNode:
        x = y.left
        assert x is not None
        tail = x.right
        x.right = y
        y.left = tail
        self._update(y)
        self._update(x)
        return x

    def _rebalance(self, node: AVLNode) -> AVLNode:
        self._update(node)
        balance = self._bf(node)
        if balance > 1:
            if self._bf(node.left) < 0:
                node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance < -1:
            if self._bf(node.right) > 0:
                node.right = self._right_rotate(node.right)
            return self._left_rotate(node)
        return node

    def _insert(self, node: Optional[AVLNode], key: int) -> AVLNode:
        if node is None:
            return AVLNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node
        return self._rebalance(node)

    def _min_node(self, node: AVLNode) -> AVLNode:
        while node.left is not None:
            node = node.left
        return node

    def _delete(self, node: Optional[AVLNode], key: int) -> Optional[AVLNode]:
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            succ = self._min_node(node.right)
            node.key = succ.key
            node.right = self._delete(node.right, succ.key)
        return self._rebalance(node)


if __name__ == "__main__":
    tree = AVL()
    for key in [10, 20, 30, 40, 50, 25]:
        tree.insert(key)
        print("after insert", key, "inorder:", tree.inorder(), "root:", tree.root.key)
    tree.delete(40)
    print("after delete 40:", tree.inorder(), "root:", tree.root.key)
    print("search 25:", tree.search(25), "search 40:", tree.search(40))

"""Задача 1. Бинарное дерево поиска и шесть обходов.

Подробное объяснение, сложность и визуализация:
см. README.md
"""

from typing import List, Optional


class TreeNode:
    """Узел бинарного дерева."""

    def __init__(
        self,
        value: int,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.value = value
        self.left = left
        self.right = right


def _require_int(value: object) -> int:
    if not isinstance(value, int) or isinstance(value, bool):
        raise TypeError(
            f"ожидалось целое число, получено: {type(value).__name__}"
        )
    return value


class BST:
    """Бинарное дерево поиска. Равные значения идут в правое поддерево."""

    def __init__(self) -> None:
        self.root: Optional[TreeNode] = None

    def insert(self, value: int) -> None:
        """Вставляет значение, сохраняя свойство BST."""
        value = _require_int(value)
        self.root = self._insert(self.root, value)

    def _insert(self, node: Optional[TreeNode], value: int) -> TreeNode:
        if node is None:
            return TreeNode(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)
        return node

    def preorder(self) -> List[int]:
        """Корень, левое, правое."""
        out: List[int] = []
        self._preorder(self.root, out)
        return out

    def _preorder(self, node: Optional[TreeNode], out: List[int]) -> None:
        if node is None:
            return
        out.append(node.value)
        self._preorder(node.left, out)
        self._preorder(node.right, out)

    def inorder(self) -> List[int]:
        """Левое, корень, правое. Для BST это возрастающий порядок."""
        out: List[int] = []
        self._inorder(self.root, out)
        return out

    def _inorder(self, node: Optional[TreeNode], out: List[int]) -> None:
        if node is None:
            return
        self._inorder(node.left, out)
        out.append(node.value)
        self._inorder(node.right, out)

    def postorder(self) -> List[int]:
        """Левое, правое, корень."""
        out: List[int] = []
        self._postorder(self.root, out)
        return out

    def _postorder(self, node: Optional[TreeNode], out: List[int]) -> None:
        if node is None:
            return
        self._postorder(node.left, out)
        self._postorder(node.right, out)
        out.append(node.value)

    def reverse_preorder(self) -> List[int]:
        """Корень, правое, левое."""
        out: List[int] = []
        self._reverse_preorder(self.root, out)
        return out

    def _reverse_preorder(self, node: Optional[TreeNode], out: List[int]) -> None:
        if node is None:
            return
        out.append(node.value)
        self._reverse_preorder(node.right, out)
        self._reverse_preorder(node.left, out)

    def reverse_inorder(self) -> List[int]:
        """Правое, корень, левое. Для BST это убывающий порядок."""
        out: List[int] = []
        self._reverse_inorder(self.root, out)
        return out

    def _reverse_inorder(self, node: Optional[TreeNode], out: List[int]) -> None:
        if node is None:
            return
        self._reverse_inorder(node.right, out)
        out.append(node.value)
        self._reverse_inorder(node.left, out)

    def reverse_postorder(self) -> List[int]:
        """Правое, левое, корень."""
        out: List[int] = []
        self._reverse_postorder(self.root, out)
        return out

    def _reverse_postorder(self, node: Optional[TreeNode], out: List[int]) -> None:
        if node is None:
            return
        self._reverse_postorder(node.right, out)
        self._reverse_postorder(node.left, out)
        out.append(node.value)


if __name__ == "__main__":
    tree = BST()
    for value in [8, 3, 10, 1, 6, 14, 4, 7]:
        tree.insert(value)
    print("preorder:         ", tree.preorder())
    print("inorder:          ", tree.inorder())
    print("postorder:        ", tree.postorder())
    print("reverse_preorder: ", tree.reverse_preorder())
    print("reverse_inorder:  ", tree.reverse_inorder())
    print("reverse_postorder:", tree.reverse_postorder())

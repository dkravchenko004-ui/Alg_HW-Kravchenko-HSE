"""Задача 2. Проверка произвольного бинарного дерева на свойство BST.

Подробное объяснение, сложность и визуализация:
см. README.md
"""

from typing import Optional


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


def _require_node(node: object) -> None:
    if node is None:
        return
    if not (
        hasattr(node, "value")
        and hasattr(node, "left")
        and hasattr(node, "right")
    ):
        raise TypeError(
            f"ожидался узел дерева или None, получено: {type(node).__name__}"
        )
    if not isinstance(node.value, int) or isinstance(node.value, bool):
        raise TypeError(
            f"значение узла должно быть целым числом, получено: {type(node.value).__name__}"
        )


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    """True, если дерево — BST: слева строго меньше, справа не меньше."""
    _require_node(root)
    return _check(root, None, None)


def _check(node: Optional[TreeNode], low: Optional[int], high: Optional[int]) -> bool:
    if node is None:
        return True
    _require_node(node)
    if low is not None and node.value < low:
        return False
    if high is not None and node.value >= high:
        return False
    return _check(node.left, low, node.value) and _check(node.right, node.value, high)


if __name__ == "__main__":
    valid = TreeNode(8, TreeNode(3, TreeNode(1), TreeNode(6)), TreeNode(10))
    invalid = TreeNode(5, TreeNode(3, None, TreeNode(6)), TreeNode(7))
    print("valid tree:  ", is_valid_bst(valid))
    print("invalid tree:", is_valid_bst(invalid))
    print("empty:       ", is_valid_bst(None))

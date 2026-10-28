"""Задача 3. Проверка, сбалансировано ли дерево по высоте.

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


def is_balanced(root: Optional[TreeNode]) -> bool:
    """True, если у каждого узла высоты детей отличаются не больше чем на 1."""
    _require_node(root)
    return _height(root) >= 0


def _height(node: Optional[TreeNode]) -> int:
    """Высота поддерева или -1, если где-то уже нарушен баланс."""
    if node is None:
        return 0
    _require_node(node)
    left = _height(node.left)
    if left < 0:
        return -1
    right = _height(node.right)
    if right < 0:
        return -1
    if abs(left - right) > 1:
        return -1
    return 1 + max(left, right)


if __name__ == "__main__":
    ok = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    bad = TreeNode(
        1,
        TreeNode(2, TreeNode(4, TreeNode(6)), TreeNode(5)),
        TreeNode(3),
    )
    print("balanced:   ", is_balanced(ok))
    print("unbalanced: ", is_balanced(bad))
    print("empty:      ", is_balanced(None))

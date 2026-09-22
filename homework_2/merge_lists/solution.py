"""Задача 3. Merge lists — слияние двух отсортированных односвязных списков.

Два способа: с фиктивным элементом (dummy) и без него.
Новый список собирается перестановкой узлов исходных списков.

Подробное объяснение, сложность и визуализация:
см. README.md
"""

from typing import Iterable, List, Optional


class ListNode:
    """Узел односвязного списка."""

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode({self.val})"


def from_list(values: Iterable[int]) -> Optional[ListNode]:
    """Собирает односвязный список из последовательности чисел."""
    dummy = ListNode(0)
    current = dummy
    for value in values:
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"Ожидалось целое число, получено: {value!r}")
        current.next = ListNode(value)
        current = current.next
    return dummy.next


def to_list(head: Optional[ListNode]) -> List[int]:
    """Преобразует односвязный список в обычный Python-список."""
    result: List[int] = []
    current = head
    while current is not None:
        result.append(current.val)
        current = current.next
    return result


def merge_two_lists_dummy(
    list1: Optional[ListNode],
    list2: Optional[ListNode],
) -> Optional[ListNode]:
    """Слияние с фиктивной головой. Ответ — dummy.next."""
    dummy = ListNode(0)
    tail = dummy

    while list1 is not None and list2 is not None:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    tail.next = list1 if list1 is not None else list2
    return dummy.next


def merge_two_lists_no_dummy(
    list1: Optional[ListNode],
    list2: Optional[ListNode],
) -> Optional[ListNode]:
    """Слияние без фиктивного элемента: голову выбираем сами."""
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    if list1.val <= list2.val:
        head = list1
        list1 = list1.next
    else:
        head = list2
        list2 = list2.next

    tail = head
    while list1 is not None and list2 is not None:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    tail.next = list1 if list1 is not None else list2
    return head


if __name__ == "__main__":
    examples = [
        ([1, 2, 4], [1, 3, 4]),
        ([], [0]),
        ([1], []),
        ([5, 6], [1, 2, 3]),
    ]
    print("Демонстрация слияния списков:")
    for left, right in examples:
        merged_dummy = merge_two_lists_dummy(from_list(left), from_list(right))
        merged_plain = merge_two_lists_no_dummy(from_list(left), from_list(right))
        print(f"  {left} + {right}")
        print(f"    dummy    -> {to_list(merged_dummy)}")
        print(f"    no_dummy -> {to_list(merged_plain)}")

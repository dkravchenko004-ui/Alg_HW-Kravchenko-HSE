"""Задача 1. Стек и очередь на основе связных списков.

Подробное объяснение, сложность и визуализация:
см. README.md
"""

from typing import Any, Optional


class Node:
    """Узел односвязного списка."""

    def __init__(self, value: Any, next: Optional["Node"] = None) -> None:
        self.value = value
        self.next = next


class Stack:
    """Стек на односвязном списке. Вершина - голова списка."""

    def __init__(self) -> None:
        self._head: Optional[Node] = None
        self._size = 0

    def push(self, value: Any) -> None:
        """Кладёт элемент на вершину стека."""
        self._head = Node(value, self._head)
        self._size += 1

    def pop(self) -> Any:
        """Снимает и возвращает элемент с вершины стека."""
        if self._head is None:
            raise IndexError("pop from empty stack")
        value = self._head.value
        self._head = self._head.next
        self._size -= 1
        return value

    def peek(self) -> Any:
        """Возвращает элемент с вершины, не снимая его."""
        if self._head is None:
            raise IndexError("peek from empty stack")
        return self._head.value

    def is_empty(self) -> bool:
        return self._head is None

    def size(self) -> int:
        return self._size

    def __len__(self) -> int:
        return self._size


class Queue:
    """Очередь на односвязном списке. Голова - выход, хвост - вход."""

    def __init__(self) -> None:
        self._head: Optional[Node] = None
        self._tail: Optional[Node] = None
        self._size = 0

    def enqueue(self, value: Any) -> None:
        """Добавляет элемент в конец очереди."""
        node = Node(value)
        if self._tail is None:
            self._head = self._tail = node
        else:
            self._tail.next = node
            self._tail = node
        self._size += 1

    def dequeue(self) -> Any:
        """Извлекает и возвращает элемент из начала очереди."""
        if self._head is None:
            raise IndexError("dequeue from empty queue")
        value = self._head.value
        self._head = self._head.next
        if self._head is None:
            self._tail = None
        self._size -= 1
        return value

    def peek(self) -> Any:
        """Возвращает элемент из начала очереди, не извлекая его."""
        if self._head is None:
            raise IndexError("peek from empty queue")
        return self._head.value

    def is_empty(self) -> bool:
        return self._head is None

    def size(self) -> int:
        return self._size

    def __len__(self) -> int:
        return self._size


if __name__ == "__main__":
    print("Стек:")
    stack = Stack()
    for x in (1, 2, 3):
        stack.push(x)
        print(f"  push({x}), вершина={stack.peek()}, size={stack.size()}")
    while not stack.is_empty():
        print(f"  pop() -> {stack.pop()}")

    print("Очередь:")
    queue = Queue()
    for x in (1, 2, 3):
        queue.enqueue(x)
        print(f"  enqueue({x}), начало={queue.peek()}, size={queue.size()}")
    while not queue.is_empty():
        print(f"  dequeue() -> {queue.dequeue()}")

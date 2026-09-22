"""Тесты для задачи 1: стек и очередь на связных списках."""

import unittest
from homework_2.stack_vs_queue.solution import Queue, Stack


class TestStack(unittest.TestCase):
    """Набор тестов для стека."""

    def test_empty_stack(self):
        """Пустой стек: размер 0, pop и peek недопустимы."""
        stack = Stack()
        self.assertTrue(stack.is_empty())
        self.assertEqual(stack.size(), 0)
        self.assertEqual(len(stack), 0)
        with self.assertRaises(IndexError):
            stack.pop()
        with self.assertRaises(IndexError):
            stack.peek()

    def test_lifo_order(self):
        """Элементы снимаются в обратном порядке."""
        stack = Stack()
        for value in (1, 2, 3, 4, 5):
            stack.push(value)
        self.assertEqual([stack.pop() for _ in range(5)], [5, 4, 3, 2, 1])
        self.assertTrue(stack.is_empty())

    def test_peek_does_not_remove(self):
        """peek не меняет размер стека."""
        stack = Stack()
        stack.push(10)
        stack.push(20)
        self.assertEqual(stack.peek(), 20)
        self.assertEqual(stack.size(), 2)
        self.assertEqual(stack.peek(), 20)
        self.assertEqual(stack.pop(), 20)
        self.assertEqual(stack.peek(), 10)

    def test_interleaved_push_pop(self):
        """Чередование push и pop."""
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.pop(), 1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.pop(), 3)
        stack.push(4)
        stack.push(5)
        self.assertEqual(stack.pop(), 5)
        self.assertEqual(stack.pop(), 4)
        self.assertEqual(stack.pop(), 2)
        self.assertTrue(stack.is_empty())

    def test_reuse_after_emptying(self):
        """После полного опустошения стек снова работает."""
        stack = Stack()
        stack.push("a")
        stack.push("b")
        stack.pop()
        stack.pop()
        stack.push("c")
        self.assertEqual(stack.peek(), "c")
        self.assertEqual(stack.size(), 1)
        self.assertEqual(stack.pop(), "c")

    def test_various_value_types(self):
        """В стек можно класть разные типы, в том числе None."""
        stack = Stack()
        stack.push(None)
        stack.push("x")
        stack.push(3.14)
        stack.push((1, 2))
        self.assertEqual(stack.pop(), (1, 2))
        self.assertEqual(stack.pop(), 3.14)
        self.assertEqual(stack.pop(), "x")
        self.assertIsNone(stack.pop())

    def test_size_tracks_operations(self):
        """size меняется после каждого push и pop."""
        stack = Stack()
        for i in range(10):
            stack.push(i)
            self.assertEqual(stack.size(), i + 1)
        for i in range(10):
            stack.pop()
            self.assertEqual(stack.size(), 9 - i)


class TestQueue(unittest.TestCase):
    """Набор тестов для очереди."""

    def test_empty_queue(self):
        """Пустая очередь: размер 0, dequeue и peek недопустимы."""
        queue = Queue()
        self.assertTrue(queue.is_empty())
        self.assertEqual(queue.size(), 0)
        self.assertEqual(len(queue), 0)
        with self.assertRaises(IndexError):
            queue.dequeue()
        with self.assertRaises(IndexError):
            queue.peek()

    def test_fifo_order(self):
        """Элементы выходят в том же порядке, в котором входили."""
        queue = Queue()
        for value in (1, 2, 3, 4, 5):
            queue.enqueue(value)
        self.assertEqual([queue.dequeue() for _ in range(5)], [1, 2, 3, 4, 5])
        self.assertTrue(queue.is_empty())

    def test_peek_does_not_remove(self):
        """peek не меняет размер очереди."""
        queue = Queue()
        queue.enqueue(10)
        queue.enqueue(20)
        self.assertEqual(queue.peek(), 10)
        self.assertEqual(queue.size(), 2)
        self.assertEqual(queue.peek(), 10)
        self.assertEqual(queue.dequeue(), 10)
        self.assertEqual(queue.peek(), 20)

    def test_interleaved_enqueue_dequeue(self):
        """Чередование enqueue и dequeue."""
        queue = Queue()
        queue.enqueue(1)
        self.assertEqual(queue.dequeue(), 1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.dequeue(), 2)
        queue.enqueue(4)
        self.assertEqual(queue.dequeue(), 3)
        self.assertEqual(queue.dequeue(), 4)
        self.assertTrue(queue.is_empty())

    def test_reuse_after_emptying(self):
        """После полного опустошения очередь снова принимает элементы."""
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.dequeue()
        queue.dequeue()
        self.assertTrue(queue.is_empty())
        queue.enqueue(7)
        queue.enqueue(8)
        self.assertEqual(queue.peek(), 7)
        self.assertEqual(queue.dequeue(), 7)
        self.assertEqual(queue.dequeue(), 8)

    def test_single_element(self):
        """Один элемент — одновременно голова и хвост."""
        queue = Queue()
        queue.enqueue(42)
        self.assertEqual(queue.peek(), 42)
        self.assertEqual(queue.size(), 1)
        self.assertEqual(queue.dequeue(), 42)
        self.assertTrue(queue.is_empty())
        with self.assertRaises(IndexError):
            queue.dequeue()

    def test_various_value_types(self):
        """В очередь можно класть разные типы."""
        queue = Queue()
        queue.enqueue(None)
        queue.enqueue("x")
        queue.enqueue([1, 2])
        self.assertIsNone(queue.dequeue())
        self.assertEqual(queue.dequeue(), "x")
        self.assertEqual(queue.dequeue(), [1, 2])

    def test_size_tracks_operations(self):
        """size меняется после каждого enqueue и dequeue."""
        queue = Queue()
        for i in range(10):
            queue.enqueue(i)
            self.assertEqual(queue.size(), i + 1)
        for i in range(10):
            queue.dequeue()
            self.assertEqual(queue.size(), 9 - i)


if __name__ == "__main__":
    unittest.main()

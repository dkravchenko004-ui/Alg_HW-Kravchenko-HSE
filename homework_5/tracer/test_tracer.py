"""Тесты для задачи 1: декоратор trace."""

import io
import unittest
from contextlib import redirect_stdout

from homework_5.tracer.solution import trace


class TestTrace(unittest.TestCase):
    """Набор тестов для декоратора trace."""

    def setUp(self):
        trace.depth = 0

    def test_factorial_trace_text(self):
        """Вход, отступ и возврат с результатом для factorial(3)."""

        @trace
        def factorial(n):
            if n <= 1:
                return 1
            return n * factorial(n - 1)

        buf = io.StringIO()
        with redirect_stdout(buf):
            result = factorial(3)
        self.assertEqual(result, 6)
        self.assertEqual(
            buf.getvalue(),
            "-> factorial(3)\n"
            "  -> factorial(2)\n"
            "    -> factorial(1)\n"
            "    <- factorial(1) = 1\n"
            "  <- factorial(2) = 2\n"
            "<- factorial(3) = 6\n",
        )

    def test_depth_indent_grows(self):
        """Чем глубже вызов, тем больше пробелов в начале строки."""

        @trace
        def countdown(n):
            if n == 0:
                return 0
            return countdown(n - 1)

        buf = io.StringIO()
        with redirect_stdout(buf):
            countdown(2)
        lines = buf.getvalue().splitlines()
        self.assertTrue(lines[0].startswith("-> "))
        self.assertTrue(lines[1].startswith("  -> "))
        self.assertTrue(lines[2].startswith("    -> "))

    def test_returns_original_value(self):
        """Декоратор не меняет ответ функции."""

        @trace
        def add(a, b):
            return a + b

        with redirect_stdout(io.StringIO()):
            self.assertEqual(add(2, 3), 5)

    def test_base_case_only(self):
        """Один вызов без рекурсии: вход и сразу выход."""

        @trace
        def const():
            return 42

        buf = io.StringIO()
        with redirect_stdout(buf):
            self.assertEqual(const(), 42)
        self.assertEqual(buf.getvalue(), "-> const()\n<- const() = 42\n")

    def test_kwargs_in_call(self):
        """Именованные аргументы видны в печати."""

        @trace
        def greet(name, times=1):
            return name * times

        buf = io.StringIO()
        with redirect_stdout(buf):
            greet("a", times=2)
        text = buf.getvalue()
        self.assertIn("times=2", text)
        self.assertIn("= 'aa'", text)

    def test_depth_resets_after_call(self):
        """После выхода из рекурсии глубина снова 0."""

        @trace
        def fact(n):
            if n <= 1:
                return 1
            return n * fact(n - 1)

        with redirect_stdout(io.StringIO()):
            fact(4)
        self.assertEqual(trace.depth, 0)

    def test_exception_still_resets_depth(self):
        """Ошибка внутри не оставляет глубину сдвинутой."""

        @trace
        def boom(n):
            if n == 0:
                raise ValueError("zero")
            return boom(n - 1)

        with redirect_stdout(io.StringIO()):
            with self.assertRaises(ValueError):
                boom(2)
        self.assertEqual(trace.depth, 0)


if __name__ == "__main__":
    unittest.main()

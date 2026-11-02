"""Задача 1. Декоратор, который печатает стек вызовов рекурсии.

Подробное объяснение, сложность и визуализация:
см. README.md
"""

from functools import wraps
from typing import Any, Callable


def trace(func: Callable) -> Callable:
    """Печатает вход в функцию, отступ по глубине и возврат с результатом."""

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        indent = "  " * trace.depth
        call = _format_call(func.__name__, args, kwargs)
        print(f"{indent}-> {call}")
        trace.depth += 1
        try:
            result = func(*args, **kwargs)
        finally:
            trace.depth -= 1
        print(f"{indent}<- {call} = {result!r}")
        return result

    return wrapper


trace.depth = 0


def _format_call(name: str, args: tuple, kwargs: dict) -> str:
    parts = [repr(arg) for arg in args]
    parts.extend(f"{key}={value!r}" for key, value in kwargs.items())
    return f"{name}({', '.join(parts)})"


if __name__ == "__main__":

    @trace
    def factorial(n):
        if n <= 1:
            return 1
        return n * factorial(n - 1)

    print(factorial(3))

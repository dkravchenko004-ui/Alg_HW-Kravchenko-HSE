"""Задача 2. Anagrams — группировка слов-анаграмм.

Подробное объяснение, сложность и визуализация:
см. README.md
"""

from typing import Iterable, List, Sequence, Union


def group_anagrams(words: Union[str, Sequence[str], Iterable[str]]) -> List[List[str]]:
    """Собирает анаграммы в группы. Порядок групп — по первому вхождению ключа."""
    if isinstance(words, str):
        items = words.split()
    elif isinstance(words, Iterable) and not isinstance(words, (bytes, bytearray)):
        items = list(words)
    else:
        raise TypeError(
            f"ожидалась строка или последовательность слов, получено: {type(words).__name__}"
        )

    for item in items:
        if not isinstance(item, str):
            raise TypeError(f"элементы должны быть строками, получено: {item!r}")

    groups = {}
    order = []
    for word in items:
        key = "".join(sorted(word))
        if key not in groups:
            groups[key] = []
            order.append(key)
        groups[key].append(word)

    return [groups[key] for key in order]


if __name__ == "__main__":
    examples = [
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        ["abc", "cba", "xyz"],
        [],
        ["a"],
    ]
    print("Демонстрация работы функции group_anagrams:")
    for words in examples:
        print(f"  {words} -> {group_anagrams(words)}")

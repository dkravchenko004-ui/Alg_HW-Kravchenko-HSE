"""Задача 3. Хеш-таблица на списках (без dict).

Подробное объяснение, сложность и визуализация:
см. README.md
"""

from typing import Any, List, Optional


class HashTable:
    """Хеш-таблица с цепочками. Корзины и пары ключ-значение хранятся в list."""

    def __init__(self, capacity: int = 8) -> None:
        if not isinstance(capacity, int) or isinstance(capacity, bool) or capacity < 1:
            raise ValueError("ёмкость должна быть целым числом >= 1")
        self._capacity = capacity
        self._size = 0
        self._buckets: List[List[List[Any]]] = [[] for _ in range(capacity)]

    def _index(self, key: Any) -> int:
        return hash(key) % self._capacity

    def _find_pair(self, key: Any) -> Optional[List[Any]]:
        bucket = self._buckets[self._index(key)]
        for pair in bucket:
            if pair[0] == key:
                return pair
        return None

    def put(self, key: Any, value: Any) -> None:
        """Вставляет пару или обновляет значение, если ключ уже есть."""
        pair = self._find_pair(key)
        if pair is not None:
            pair[1] = value
            return
        self._buckets[self._index(key)].append([key, value])
        self._size += 1
        if self._size * 4 > self._capacity * 3:
            self._rehash(self._capacity * 2)

    def get(self, key: Any) -> Any:
        """Возвращает значение по ключу."""
        pair = self._find_pair(key)
        if pair is None:
            raise KeyError(key)
        return pair[1]

    def delete(self, key: Any) -> Any:
        """Удаляет ключ и возвращает его значение."""
        bucket = self._buckets[self._index(key)]
        for i, pair in enumerate(bucket):
            if pair[0] == key:
                removed = bucket.pop(i)
                self._size -= 1
                return removed[1]
        raise KeyError(key)

    def contains(self, key: Any) -> bool:
        return self._find_pair(key) is not None

    def size(self) -> int:
        return self._size

    def __len__(self) -> int:
        return self._size

    def __contains__(self, key: Any) -> bool:
        return self.contains(key)

    def load_factor(self) -> float:
        return self._size / self._capacity

    def _rehash(self, new_capacity: int) -> None:
        old_buckets = self._buckets
        self._capacity = new_capacity
        self._size = 0
        self._buckets = [[] for _ in range(new_capacity)]
        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)


if __name__ == "__main__":
    table = HashTable(capacity=4)
    table.put("apple", 10)
    table.put("banana", 20)
    table.put("apple", 15)
    print("get apple:", table.get("apple"))
    print("contains banana:", table.contains("banana"))
    print("size:", table.size())
    table.delete("banana")
    print("after delete banana, size:", table.size())
    try:
        table.get("banana")
    except KeyError:
        print("banana removed")

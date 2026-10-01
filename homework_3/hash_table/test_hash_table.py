"""Тесты для задачи 3: хеш-таблица на списках."""

import unittest
from homework_3.hash_table.solution import HashTable


class TestHashTable(unittest.TestCase):
    """Набор тестов для HashTable."""

    def test_put_and_get(self):
        """Вставка и поиск по ключу."""
        table = HashTable()
        table.put("a", 1)
        table.put("b", 2)
        self.assertEqual(table.get("a"), 1)
        self.assertEqual(table.get("b"), 2)
        self.assertEqual(table.size(), 2)

    def test_update_existing_key(self):
        """Повторная вставка того же ключа обновляет значение, размер не растёт."""
        table = HashTable()
        table.put("x", 10)
        table.put("x", 20)
        self.assertEqual(table.get("x"), 20)
        self.assertEqual(table.size(), 1)

    def test_delete(self):
        """Удаление убирает ключ и уменьшает размер."""
        table = HashTable()
        table.put("a", 1)
        table.put("b", 2)
        self.assertEqual(table.delete("a"), 1)
        self.assertEqual(table.size(), 1)
        self.assertFalse(table.contains("a"))
        self.assertTrue(table.contains("b"))

    def test_missing_key(self):
        """Поиск и удаление отсутствующего ключа — KeyError."""
        table = HashTable()
        table.put("a", 1)
        with self.assertRaises(KeyError):
            table.get("z")
        with self.assertRaises(KeyError):
            table.delete("z")

    def test_empty_table(self):
        """Пустая таблица: размер 0, ключей нет."""
        table = HashTable()
        self.assertEqual(table.size(), 0)
        self.assertEqual(len(table), 0)
        self.assertFalse(table.contains("a"))
        with self.assertRaises(KeyError):
            table.get("a")

    def test_collisions(self):
        """Ключи, попадающие в одну корзину, оба находятся."""
        table = HashTable(capacity=4)
        keys = []
        for n in range(40):
            if hash(n) % 4 == 0:
                keys.append(n)
            if len(keys) == 3:
                break
        self.assertGreaterEqual(len(keys), 2)
        for i, key in enumerate(keys):
            table.put(key, i * 10)
        for i, key in enumerate(keys):
            self.assertEqual(table.get(key), i * 10)
        table.delete(keys[0])
        self.assertFalse(table.contains(keys[0]))
        self.assertEqual(table.get(keys[1]), 10)

    def test_resize_keeps_values(self):
        """После роста таблицы старые пары на месте."""
        table = HashTable(capacity=4)
        for i in range(20):
            table.put(i, i * i)
        self.assertEqual(table.size(), 20)
        self.assertGreater(table._capacity, 4)
        for i in range(20):
            self.assertEqual(table.get(i), i * i)

    def test_contains_operator(self):
        """Оператор in."""
        table = HashTable()
        table.put(5, "five")
        self.assertIn(5, table)
        self.assertNotIn(6, table)

    def test_int_and_string_keys(self):
        """Разные типы ключей."""
        table = HashTable()
        table.put(1, "int")
        table.put("1", "str")
        self.assertEqual(table.get(1), "int")
        self.assertEqual(table.get("1"), "str")

    def test_delete_then_put_again(self):
        """После удаления ключ можно вставить снова."""
        table = HashTable()
        table.put("k", 1)
        table.delete("k")
        table.put("k", 2)
        self.assertEqual(table.get("k"), 2)
        self.assertEqual(table.size(), 1)

    def test_invalid_capacity(self):
        """Ёмкость меньше 1 недопустима."""
        with self.assertRaises(ValueError):
            HashTable(capacity=0)
        with self.assertRaises(ValueError):
            HashTable(capacity=-3)

    def test_storage_is_lists(self):
        """Данные лежат в list, не в dict."""
        table = HashTable(capacity=4)
        table.put("a", 1)
        self.assertIsInstance(table._buckets, list)
        for bucket in table._buckets:
            self.assertIsInstance(bucket, list)


if __name__ == "__main__":
    unittest.main()

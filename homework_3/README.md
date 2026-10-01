# Homework 3

Решения трёх задач на Python: two sum, группировка анаграмм,
своя хеш-таблица на списках.

В каждой задаче есть:

- `solution.py` — код решения
- `test_*.py` — тесты (`unittest`)
- `README.md` — идея алгоритма, оценка сложности `O(...)`, пошаговая визуализация

## Структура

```text
homework_3/
├── README.md
├── two_sum/
│   ├── solution.py
│   ├── test_two_sum.py
│   └── README.md
├── anagrams/
│   ├── solution.py
│   ├── test_anagrams.py
│   └── README.md
└── hash_table/
    ├── solution.py
    ├── test_hash_table.py
    └── README.md
```

## Требования

- Python 3.8+
- Стандартная библиотека (`unittest`) — дополнительные пакеты не нужны
- Сторонние библиотеки не используются
- В хеш-таблице данные хранятся только в `list`, без `dict`

Некорректный ввод — исключение (`TypeError`, `ValueError`, `KeyError`).

## Как запустить тесты

Команды выполнять из **корня репозитория** (директории, в которой лежит папка `homework_3`).

Все тесты:

```bash
python -m unittest discover homework_3
```

Подробный вывод:

```bash
python -m unittest discover homework_3 -v
```

По задачам:

```bash
python -m unittest homework_3.two_sum.test_two_sum
python -m unittest homework_3.anagrams.test_anagrams
python -m unittest homework_3.hash_table.test_hash_table
```

Если установлен `pytest`:

```bash
python -m pytest homework_3 -v
```

Ожидаемый результат: `Ran 31 tests` => `OK`.

## Задачи

| Папка | Задача | Кратко |
| ----- | ------ | ------ |
| [two_sum/](two_sum/) | Two sum | Индексы двух элементов с суммой `k` |
| [anagrams/](anagrams/) | Anagrams | Группы слов-анаграмм |
| [hash_table/](hash_table/) | Хеш-таблица | Своя таблица: вставка, поиск, удаление |

Подробности по каждой задаче — в `README.md` соответствующей папки.

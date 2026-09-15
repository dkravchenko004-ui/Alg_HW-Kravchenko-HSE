# Homework 1

Решения трёх задач на Python: палиндром, максимальная чётная сумма, количество простых чисел.

В каждой задаче есть:
- `solution.py` — код решения
- `test_*.py` — тесты (`unittest`)
- `README_объяснение_сложность_визуализация.md` — идея алгоритма, оценка сложности `O(...)`, пошаговая визуализация

## Структура

```text
homework_1/
├── README.md
├── palindrome/
│   ├── solution.py
│   ├── test_palindrome.py
│   └── README_объяснение_сложность_визуализация.md
├── sum/
│   ├── solution.py
│   ├── test_sum.py
│   └── README_объяснение_сложность_визуализация.md
└── prime/
    ├── solution.py
    ├── test_prime.py
    └── README_объяснение_сложность_визуализация.md
```

## Требования

- Python 3.8+
- Стандартная библиотека (`unittest`) — дополнительные пакеты не нужны

## Как запустить тесты

Команды выполнять из **корня репозитория** (директории, в которой лежит папка `homework_1`).

Все тесты:

```bash
python -m unittest discover homework_1
```

Подробный вывод:

```bash
python -m unittest discover homework_1 -v
```

По задачам:

```bash
python -m unittest homework_1.palindrome.test_palindrome
python -m unittest homework_1.sum.test_sum
python -m unittest homework_1.prime.test_prime
```

Если установлен `pytest`:

```bash
python -m pytest homework_1 -v
```

Ожидаемый результат: `Ran 25 tests` => `OK`.

## Задачи

| Папка | Задача | Кратко |
|-------|--------|--------|
| [`palindrome/`](palindrome/) | Палиндром | Проверка числа **без строк** |
| [`sum/`](sum/) | Сумма | Максимальная сумма элементов, делящаяся на 2 |
| [`prime/`](prime/) | Простые числа | Количество простых строго меньше `N` |

Подробности по каждой задаче — в соответствующем `README_объяснение_сложность_визуализация.md`.

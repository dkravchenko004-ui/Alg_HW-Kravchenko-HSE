# Homework 5

Три задачи: декоратор трассировки рекурсии, перестановки, АВЛ-дерево.

Сдача в репозитории:

- `/homework_5/tracer/`
- `/homework_5/permutations/`
- `/homework_5/AVL/`

В каждой задаче есть:

- `solution.py` — код решения
- `test_*.py` — тесты (`unittest`)
- `README.md` — идея, сложность `O(...)`, пошаговая визуализация

## Структура

```text
homework_5/
├── README.md
├── tracer/
├── permutations/
└── AVL/
```

## Требования

- Python 3.8+
- Стандартная библиотека (`unittest`) — дополнительные пакеты не нужны
- Сторонние библиотеки не используются

Некорректный ввод — исключение (`TypeError`, `KeyError`).

## Как запустить тесты

Команды выполнять из **корня репозитория**.

```bash
python -m unittest discover homework_5
python -m unittest discover homework_5 -v
```

По задачам:

```bash
python -m unittest homework_5.tracer.test_tracer
python -m unittest homework_5.permutations.test_permutations
python -m unittest homework_5.AVL.test_avl
```

Если установлен `pytest`:

```bash
python -m pytest homework_5 -v
```

Ожидаемый результат: `Ran 29 tests` => `OK`.

## Задачи

| Папка | Задача | Кратко |
| ----- | ------ | ------ |
| [tracer/](tracer/) | Tracer | декоратор стека рекурсии |
| [permutations/](permutations/) | Permutations | все перестановки, с `trace` |
| [AVL/](AVL/) | AVL | вставка, удаление, поиск |

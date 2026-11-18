# Homework 6

Три задачи на сортировки: сравнение рекурсивных merge/quick, их
итеративные версии и k-й по величине через quickselect.

Сдача в репозитории:

- `/homework_6/compare/`
- `/homework_6/iterative/`
- `/homework_6/kth/`

В каждой задаче есть:

- `solution.py` — код решения
- `test_*.py` — тесты (`unittest`)
- `README.md` — идея, сложность `O(...)`, пошаговая визуализация

## Структура

```text
homework_6/
├── README.md
├── compare/
├── iterative/
└── kth/
```

## Требования

- Python 3.8+
- Стандартная библиотека (`unittest`) — дополнительные пакеты не нужны
- Сторонние библиотеки не используются

Некорректный ввод — исключение (`TypeError`, `ValueError`).

Quicksort везде как на лекции: опорный ставим так, чтобы меньшие были
до него, большие или равные — после. Опорный на отрезке — последний
элемент.

## Как запустить тесты

Команды выполнять из **корня репозитория**.

```bash
python -m unittest discover homework_6
python -m unittest discover homework_6 -v
```

По задачам:

```bash
python -m unittest homework_6.compare.test_compare
python -m unittest homework_6.iterative.test_iterative
python -m unittest homework_6.kth.test_kth
```

Если установлен `pytest`:

```bash
python -m pytest homework_6 -v
```

Ожидаемый результат: `Ran 35 tests` => `OK`.

## Задачи

| Папка | Задача | Кратко |
| ----- | ------ | ------ |
| [compare/](compare/) | Compare | рекурсивные merge/quick + замер времени |
| [iterative/](iterative/) | Iterative | те же сортировки без рекурсии |
| [kth/](kth/) | K-th | k-й максимум, quickselect, без полной сортировки |

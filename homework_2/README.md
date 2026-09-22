# Homework 2

Решения трёх задач на Python: стек и очередь на связных списках, проверка
последовательности push/pop, слияние отсортированных односвязных списков.

В каждой задаче есть:

- `solution.py` — код решения
- `test_*.py` — тесты (`unittest`)
- `README.md` — идея алгоритма, оценка сложности `O(...)`, пошаговая визуализация

## Структура

```text
homework_2/
├── README.md
├── stack_vs_queue/
│   ├── solution.py
│   ├── test_stack_vs_queue.py
│   └── README.md
├── validate/
│   ├── solution.py
│   ├── test_validate.py
│   └── README.md
└── merge_lists/
    ├── solution.py
    ├── test_merge_lists.py
    └── README.md
```



## Требования

- Python 3.8+
- Стандартная библиотека (`unittest`) — дополнительные пакеты не нужны
- Сторонние библиотеки не используются

Некорректный ввод везде обрабатывается одинаково: бросаем исключение
(`IndexError`, `ValueError`, `TypeError`). Штатный пустой список в merge —
это не ошибка, возвращаем второй список или `None`.

## Как запустить тесты

Команды выполнять из **корня репозитория** (директории, в которой лежит папка `homework_2`).

Все тесты:

```bash
python -m unittest discover homework_2
```

Подробный вывод:

```bash
python -m unittest discover homework_2 -v
```

По задачам:

```bash
python -m unittest homework_2.stack_vs_queue.test_stack_vs_queue
python -m unittest homework_2.validate.test_validate
python -m unittest homework_2.merge_lists.test_merge_lists
```

Если установлен `pytest`:

```bash
python -m pytest homework_2 -v
```

Ожидаемый результат: `Ran 37 tests` => `OK`.

## Задачи


| Папка                                | Задача         | Кратко                                                     |
| ------------------------------------ | -------------- | ---------------------------------------------------------- |
| `[stack_vs_queue/](stack_vs_queue/)` | Stack vs Queue | Стек (LIFO) и очередь (FIFO) на односвязных списках        |
| `[validate/](validate/)`             | Validate       | Можно ли получить `popped` операциями push/pop из `pushed` |
| `[merge_lists/](merge_lists/)`       | Merge lists    | Слияние двух отсортированных списков: с dummy и без        |


Подробности по каждой задаче — в `README.md` соответствующей папки.
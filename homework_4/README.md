# Homework 4

Решения трёх задач на Python про бинарные деревья поиска и обходы.

Сдача: папка `homework_4/Binary_Tree/` в репозитории.

В каждой задаче есть:

- `solution.py` — код решения
- `test_*.py` — тесты (`unittest`)
- `README.md` — идея алгоритма, оценка сложности `O(...)`, пошаговая визуализация дерева

## Структура

```text
homework_4/
├── README.md
└── Binary_Tree/
    ├── README.md
    ├── tree_traversal/
    │   ├── solution.py
    │   ├── test_tree_traversal.py
    │   └── README.md
    ├── validate_bst/
    │   ├── solution.py
    │   ├── test_validate_bst.py
    │   └── README.md
    └── balanced_tree/
        ├── solution.py
        ├── test_balanced_tree.py
        └── README.md
```

## Требования

- Python 3.8+
- Стандартная библиотека (`unittest`) — дополнительные пакеты не нужны
- Сторонние библиотеки не используются

Некорректный ввод — исключение (`TypeError`).

## Как запустить тесты

Команды выполнять из **корня репозитория** (директории, в которой лежит папка `homework_4`).

Все тесты:

```bash
python -m unittest discover homework_4
```

Подробный вывод:

```bash
python -m unittest discover homework_4 -v
```

По задачам:

```bash
python -m unittest homework_4.Binary_Tree.tree_traversal.test_tree_traversal
python -m unittest homework_4.Binary_Tree.validate_bst.test_validate_bst
python -m unittest homework_4.Binary_Tree.balanced_tree.test_balanced_tree
```

Если установлен `pytest`:

```bash
python -m pytest homework_4 -v
```

Ожидаемый результат: `Ran 32 tests` => `OK`.

## Задачи

| Папка | Задача | Кратко |
| ----- | ------ | ------ |
| [Binary_Tree/tree_traversal/](Binary_Tree/tree_traversal/) | Tree Traversal | BST, вставка, шесть обходов |
| [Binary_Tree/validate_bst/](Binary_Tree/validate_bst/) | Validate BST | дерево является BST или нет |
| [Binary_Tree/balanced_tree/](Binary_Tree/balanced_tree/) | Balanced Binary Tree | баланс по высоте |

Подробности по каждой задаче — в `README.md` соответствующей папки.

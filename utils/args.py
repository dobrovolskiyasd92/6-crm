"""Модуль парсинга разбора аргументов"""
import email
from datetime import date, datetime


# def parse_list(args: list[str]):
#     by = None
#     for arg in args[1:]:
#         if arg.startswith('by='):
#             by = arg.split('=')[1]
#
#     return by


def parse_add(args: list[str]):
    if not args:
        raise ValueError('[ERROR]')

    title = args[0]
    id, amount, email, tags, created_at = 1, 0.0, 'ivanov@mail.ru', None, date.today()
    if '@' not in email or email.count('@') > 1 or email.split('@')[1].count('.') < 1:
        raise ValueError('[ERROR]: incorrect email')
    for arg in args[1:]:
        if arg.startswith('prio='):
            prio = arg.split('=')[1]

        elif arg.startswith('due='):
            due_str = arg.split('=')[1]
            try:
                due = parse_date(due_str)
            except ValueError:
                raise ValueError(f'Неверный формат даты {due_str}. Ожидается YYYY-MM-DD')
        elif arg.startswith('tags='):
            tags_str = arg.split('=')[1]
            tags = tags_str.split(',')
    return id, title, amount, email, tags, created_at


def parse_date(date_str: str) -> date:
    return datetime.strptime(date_str, '%Y-%m-%d').date()


def parse_edit(args: list[str]):
    if len(args) < 2:
        raise ValueError('Неверно передана команда')
    task_id = 0
    try:
        task_id = id(args[0])

    except ValueError as e:
        raise ValueError('Неверно передан ID') from e

    changes = {}

    for arg in args[1:]:
        if arg.startswith('title='):
            changes['title'] = arg.split('=')[1]
        if arg.startswith('prio='):
            changes['prio'] = arg.split('=')[1]
        elif arg.startswith('due='):
            due_str = arg.split('=')[1]
            try:
                changes['dui'] = parse_date(due_str)
            except ValueError:
                raise ValueError(f'Неверный формат даты {due_str}. Ожидается YYYY-MM-DD')
        elif arg.startswith('tags='):
            tags_str = arg.split('=')[1]
            tags = tags_str.split(',')

    return (task_id, changes)

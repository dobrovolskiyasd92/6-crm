"""Модуль для получения таблицы"""
from datetime import date

from orders import Order


def format_date(d: date) -> str:
    return date.strftime(d, '%Y-%m-%d')


def stringify_table(orders: list[Order]) -> str:
    headers = ['ID', 'Название', 'Цена', 'e-mail', 'Статус', 'Теги', 'Дата создания', 'Срок выполнения', 'Дата выполения']
    rows = []
    for order in orders:
        tags = ','.join(order['tags']) if order['tags'] else '-'
        rows.append([
            str(order['id']),
            str(order['title']),
            str(order['amount']),
            str(order['email']),
            str(order['status']),
            format_date(order['created_at']),
            format_date(order['due']),
            format_date(order['closed_at']) if order['closed_at'] else '-',

        ])
    col_width = [len(h) for h in headers]
    for row in rows:
        for i, col in enumerate(col_width):
            col_width[i] = max(col_width[i], len(row[i]))

    def fmt_row(row):
        return ' | '.join(f'{col:<{col_width[i]}}' for i, col in enumerate(row))

    out = []
    out.append((fmt_row(headers)))
    out.append('-+-'.join('-' * w for w in col_width))
    for row in rows:
        out.append(fmt_row(row))

    return '\n'.join(out)

"""Модуль для просмотра списка заказов"""
from orders import Order
from utils.table import stringify_table


def list_orders(orders: list[Order]):
    subset = orders[:]
    if not subset:
        print('Список заказов пуст')
        return

    print(stringify_table(subset))
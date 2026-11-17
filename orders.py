from datetime import date
from typing import TypedDict, Optional

STATUSES = ('new', 'in_progress', 'done', 'canceled')


class Order(TypedDict):
    id: int
    title: str
    amount: float
    email: str
    status: str
    tags: list[str]
    created_at: date
    due: Optional[str]
    closed_at: date

orders: list[Order] = []


def create_order(order_id: int, order_title: str, order_amount: float, order_email: str, order_status: str,
                 order_tags: list[str], order_created_at: date, order_due=None, order_closed_at: date = None) -> Order:
    order: Order = {
        'id': order_id,
        'title': order_title,
        'amount': order_amount,
        'email': order_email,
        'status': order_status,
        'tags': order_tags,
        'created_at': order_created_at,
        'due': order_due,
        'closed_at': order_closed_at
    }

    orders.append(order)

def list_orders(orders_list, order_id: int):
   for order in orders_list:
       _print_order(order)

def edit_order(order: Order, order_title: str, order_amount: float, order_email: str):
    order['title'] = order_title
    order['amount'] = order_amount
    order['email'] = order_email
    return order

def remove_order(orders_list, order_id: int):
    for order in orders_list:
        idx = orders_list.index(order)
        if order['id'] == order_id:
            del orders_list[idx]

def _print_order(order):
    print(f'{'=' * 20}')
    print(order['title'])
    print(order['amount'])
    print(order['email'])
    print(order['status'])
    print(order['tags'])
    print(order['created_at'])
    print(order['due'])
    print(order['closed_at'])
    print(f'{'=' * 20}')

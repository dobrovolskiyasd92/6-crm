"""Module add order"""
from orders import Order, create_order
from utils.args import parse_add


def add_order(orders: list[Order], args: list[str]):
    try:

        if len(args) < 6:
            print('Invalid number of arguments. Do it: add <id> <title> <amount> <email> <tags> <created_at>')
            return

        id, title, amount, email, tags, created_at = parse_add(args)
        order = create_order(id, title, amount, email, tags, created_at)
        orders.append(order)
    except Exception as e:
        print(args, 'add_orders')
        print(e)
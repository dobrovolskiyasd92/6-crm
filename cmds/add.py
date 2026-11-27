"""Module add order"""
import datetime
from orders import Order, make_order
from utils.args import parse_args

VALID_ADD_KEYS = {'id', 'title', 'amount', 'email', 'status', 'tags', 'create_at', 'due', 'closed_at'}

def add_order(orders: list[Order], args: list):
    if not args:
        raise Exception("No args")
    raw = parse_args(args)
    # print(f'{'+'*5} {raw} {'+'*5}')

    check_keys_set = set()
    for key in raw.keys():
        check_keys_set.add(key)
    if not check_keys_set.issubset(VALID_ADD_KEYS):
        raise Exception("Invalid command. Use ...")

    if not raw.get('id'):
        raise Exception("No id")
    if not raw.get('title'):
        raise Exception("No amount")
    if not raw.get('amount'):
        raise Exception("No amount")
    if not raw.get('email'):
        raise Exception("No email")

    id_ = raw.get('id')
    title = raw.get('title')
    amount = raw.get('amount')
    email = raw.get('email')

    status, tags, create_at, due, closed_at = 'new', None, None, None, None

    if raw.get('status'):
        status = raw.get('status')
    if raw.get('tags'):
        tags = raw.get('tags')
    if raw.get('create_at'):
        create_at = raw.get('create_at')
    if raw.get('due'):
        due = raw.get('due')
    if raw.get('closed_at'):
        closed_at = raw.get('closed_at')

    order = make_order(id_, title, amount, email, status, tags, create_at, due, closed_at)
    print(order)
    orders.append(order)
    return orders

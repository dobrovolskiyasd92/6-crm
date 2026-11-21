import json
from orders import Order


def load(path):
    raw_data = {}
    try:
        with open(path, 'r', encoding='utf-8') as f:
            raw_data = json.load(f)
    except FileNotFoundError:
        print('File not found')
        return []

    except json.decoder.JSONDecodeError:
        print('Invalid JSON')
        return []

    orders: list[Order] = []
    max_id = 0
    for item in raw_data.get("orders", []):
        try:
            order: Order = {
                'id': int(item["id"]),
                'title': item["title"],
                'amount': item["amount"],
                'email': item["email"],
                'status': item["status"],
                'tags': list(item.get("tags", [])),
                'created_at': item["created_at"],
                'due': item["due"],
                'closed_at': item["closed_at"],
            }
            orders.append(order)
        except Exception as e:
            print(e)

    return orders, max_id + 1




def save(path:str, orders: list[Order]):
    data = {
        'orders': [
            {
                'id': o['id'],
                'title': o['title'],
                'amount': o['amount'],
                'email': o['email'],
                'status': o['status'],
                'tags': o['tags'],
                'created_at': o['created_at'],
                'due': o['due'],
                'closed_at': o['closed_at']
            }
            for o in orders
        ]
    }
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


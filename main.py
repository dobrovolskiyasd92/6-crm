from cmds.add import add_order
from cmds.list import list_orders
from orders import edit_order
from utils.storage import save, load


def main():
    file_path = 'orders.json'
    orders = load(file_path)
    print("Orders manager. Input 'help' for help")
    try:

        while True:
            raw_string = input("> ").strip().lower()
            parts = raw_string.split()
            cmd, args = parts[0], parts[1:]
            match cmd:
                case "help":
                    pass
                case "list":
                    list_orders(orders)
                    # print(orders)
                case "add":
                    add_order(orders, args)
                case "remove":
                    pass
                case "edit":
                    edit_order(orders, args)
                case "tag":
                    pass
                case 'status':
                    pass
                case 'quit':
                    save(file_path, orders)
                    print("Goodbye!")
                    break
                case _:
                    print("Invalid command")



    except KeyboardInterrupt:
        print("Exiting...")
    except Exception as e:
        print(f"[ERROR]: {e}")


if __name__ == "__main__":
    main()

# Итоговые команды в приложении:
# list — вывести таблицу заказов (id, title, amount, status, due).
#
#     •    --overdue,
#
#     •    --tag=... (фильтр по тегу),
#
#     •    --limit=N.
#
# add --title "..." --amount 123.45 --email user@ex.com [--due "..."] [--tags "a,b,c"
#
# remove --id <uuid> — удалить заказ по id.
#
# edit --id <uuid> [--title ...] [--amount ...] [--email ...] [--due ...] — редактирование только переданных полей.
#
# tags --id <uuid> [--add a,b] [--remove x,y] — управление тегами (множество).
#
# status --id <uuid> status — изменение статуса

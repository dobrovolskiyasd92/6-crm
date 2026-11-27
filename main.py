from cmds.help import help_command
from cmds.add import add_order


def main():
    orders = []
    print("Orders manager. Input 'help' for help")
    while True:
        try:
            raw_string = input("> ").strip()
            parts = raw_string.split()
            cmd, args = parts[0], parts[1:]

            match cmd:
                case "help":
                    help_command()
                case "list":
                    print(orders)
                case "add":
                    add_order(orders, args)
                case "remove":
                    pass
                case "edit":
                    pass
                case "tag":
                    pass
                case 'status':
                    pass
                case 'exit':
                    print("Goodbye!")
                    break
                case _:
                    print("Invalid command")



        except KeyboardInterrupt:
            print("Exiting...")
            break
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

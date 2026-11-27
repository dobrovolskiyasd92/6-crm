"""Вывод справки"""

def help_command():
    print("""
    help - Вывод справки
    add --title <title> --amount <amount> --email <email> [--status <status>] [--tags <tags>] [--created_at <created_at>] [--due <due>] [--closed_at <closed_at>] - Добавить заказ
    
    exit - Выход
    """)
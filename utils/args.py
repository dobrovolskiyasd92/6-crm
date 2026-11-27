"""Модуль парсинга разбора аргументов"""
import email
from datetime import date, datetime

def parse_date(date_str: str) -> date:
    return datetime.strptime(date_str, '%Y-%m-%d').date()


def parse_args(args: list) -> dict:
    raw_args = []
    for arg in args:
        raw_args.append(arg.replace('--', ''))
    args_dict = dict(zip(raw_args[::2], raw_args[1::2]))
    return args_dict
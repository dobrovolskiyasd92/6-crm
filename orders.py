from datetime import date
from typing import TypedDict, Optional
from uuid import UUID

from utils.validators import is_valid_email

from utils.args import parse_date

STATUSES = ('new', 'in_progress', 'done', 'canceled')
TODAY = date.today()


class Order(TypedDict):
    id: UUID
    title: str
    amount: float
    email: str
    status: str
    tags: Optional[list[str]] | type[None]
    created_at: Optional[date]
    due: Optional[date]
    closed_at: Optional[date]


def make_order(
        id_: UUID,
        title: str,
        amount: float,
        email: str,
        status: str,
        tags: Optional[list[str]] = None,
        created_at: Optional[date] = None,
        due: Optional[date] = None,
        closed_at: Optional[date] = None,
                                            ) -> Order:
    if status not in STATUSES:
        raise ValueError(f'Invalid status {status}')
    if not is_valid_email(email):
        raise ValueError(f'Invalid email {email}')

    order: Order = {
        'id': str(id_),
        'title': title,
        'amount': float(amount),
        'email': email,
        'status': status,
        'tags': tags.split(',') if tags is not None else [],
        'created_at': parse_date(created_at) if created_at else None,
        'due': parse_date(due) if due is not None else None,
        'closed_at': parse_date(closed_at) if closed_at is not None else None
    }
    return order

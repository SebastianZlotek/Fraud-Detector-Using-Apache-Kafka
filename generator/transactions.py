"""Modelowanie transakcji finansowych"""

from random import choices, randint
from string import ascii_letters, digits

account_chars: str = digits + ascii_letters


def _random_account_id() -> str:
    """Zwracanie loswego numeru konta zlozonego z 12 znakow."""
    return ''.join(choices(account_chars, k=12))


def _random_amount() -> float:
    """Zwracanie losowej sumy pieniedzy pomiedzy 1.00 a 1000.00."""
    return randint(100, 100000) / 100


def create_random_transaction() -> dict:
    """Tworzenie falszywej, losowej transakcji."""
    return {
        'source': _random_account_id(),
        'target': _random_account_id(),
        'amount': _random_amount(),
        'currency': 'USD',
    }

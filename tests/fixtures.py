import os
from datetime import date

import pytest
from decimal import Decimal

from currencies.settings import BASE_DIR
from exchange.models import CurrencyRate


def rrs_response():
    with open(os.path.join(BASE_DIR, 'tests/rss_example'), 'r') as rrs:
        content = rrs.read()
    return content


@pytest.fixture
def currency_rate():
    return CurrencyRate.objects.create(
        currency='USD',
        date=date(year=2019, month=5, day=1),
        exchange_rate=Decimal('2')
    )

from datetime import date

import pytest
from decimal import Decimal
from django.test import Client
from django.urls import reverse

from exchange.models import CurrencyRate


@pytest.mark.django_db
def test_currency_exchange(currency_rate):
    to_currency = CurrencyRate.objects.create(
        currency='ABC',
        date=date(year=2019, month=5, day=1),
        exchange_rate=Decimal('4')
    )
    amount = 100
    client = Client()
    response = client.get(
        f'{reverse("currencies-exchange-rate")}?currency1={currency_rate.currency}&currency2={to_currency.currency}&amount={amount}'
    )
    assert response.status_code == 200
    assert response.data == {
        'currency1': currency_rate.currency,
        'currency2': to_currency.currency,
        'amount': '%.4f' % amount,
        'value2': str(Decimal('200'))
    }

    # try to reverse currencies
    response = client.get(
        f'{reverse("currencies-exchange-rate")}?currency1={to_currency.currency}&currency2={currency_rate.currency}&amount={amount}'
    )
    assert response.status_code == 200
    assert response.data == {
        'currency1': to_currency.currency,
        'currency2': currency_rate.currency,
        'amount': '%.4f' % amount,
        'value2': str(Decimal('200'))
    }


@pytest.mark.django_db
def test_currency_exchange_invalid(currency_rate):
    to_currency = CurrencyRate.objects.create(
        currency='ABC',
        date=date(year=2019, month=5, day=1),
        exchange_rate=Decimal('4')
    )
    amount = 'asd'
    client = Client()
    response = client.get(
        f'{reverse("currencies-exchange-rate")}?currency1={currency_rate.currency}&currency2={to_currency.currency}&amount={amount}'
    )
    assert response.status_code == 400

    amount = 100
    response = client.get(
        f'{reverse("currencies-exchange-rate")}?currency1=NON&currency2={to_currency.currency}&amount={amount}'
    )
    assert response.status_code == 400

    response = client.get(
        f'{reverse("currencies-exchange-rate")}?currency1={to_currency.currency}&currency2={currency_rate.currency}&amount={amount}'
    )
    assert response.status_code == 200

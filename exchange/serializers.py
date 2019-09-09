from decimal import Decimal

from rest_framework.fields import CharField, SerializerMethodField, DecimalField
from rest_framework.serializers import Serializer

from exchange.models import CurrencyRate


class CurrencyRateSerializer(Serializer):
    currency1 = CharField(max_length=3)
    currency2 = CharField(max_length=3)
    amount = DecimalField(max_digits=100, decimal_places=4)
    value2 = SerializerMethodField()

    def get_value2(self, obj):
        """
        Calculates first currency in EUR and compares with other currency
        """
        from_currency = CurrencyRate.objects.filter(currency=obj['currency1']).latest('date')
        to_currency = CurrencyRate.objects.filter(currency=obj['currency2']).latest('date')
        amount = Decimal(obj['amount'])
        return str(amount * to_currency.exchange_rate / from_currency.exchange_rate)

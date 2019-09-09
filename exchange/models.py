from django.db import models

from currencies.utils.model_utils import TimestampedModel


class CurrencyRate(TimestampedModel):
    currency = models.CharField(max_length=3)
    exchange_rate = models.DecimalField(decimal_places=4, max_digits=20)
    date = models.DateField()

    class Meta:
        unique_together = ['date', 'currency']

from django.contrib import admin
from django.contrib.admin import register

from exchange.models import CurrencyRate


@register(CurrencyRate)
class CurrencyRateAdmin(admin.ModelAdmin):
    class Meta:
        fields = 'all'

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

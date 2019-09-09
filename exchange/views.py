from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from currencies import settings
from exchange.models import CurrencyRate
from exchange.scraper import ECBScraper
from exchange.serializers import CurrencyRateSerializer


class CurrenciesApiViewSet(ViewSet):
    @action(detail=False, methods=['post'])
    def scrap(self, request):
        ECBScraper().scrap()
        return Response('success', status.HTTP_200_OK)

    @action(detail=False)
    def exchange(self, request):
        from_currency = request.GET.get('currency1')
        to_currency = request.GET.get('currency2')
        amount = request.GET.get('amount')
        print(settings.DEBUG)

        available_currencies = CurrencyRate.objects.values_list('currency', flat=True).order_by('currency').distinct()
        if from_currency not in available_currencies or to_currency not in available_currencies:
            return Response(f'Available currencies are: {", ".join(available_currencies)}', status.HTTP_400_BAD_REQUEST)

        serializer = CurrencyRateSerializer(
            data={'currency1': from_currency, 'currency2': to_currency, 'amount': amount}
        )
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status.HTTP_200_OK)

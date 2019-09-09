import pytest
from unittest import mock

import feedparser

from exchange.models import CurrencyRate
from exchange.scraper import ECBScraper
from tests.fixtures import rrs_response


@pytest.mark.django_db
@mock.patch('feedparser.parse', mock.Mock(return_value=feedparser.parse(rrs_response())))
def test_single_scrap():
    scraper = ECBScraper()
    scraper.scrap_page('link')
    assert CurrencyRate.objects.count() == 5
    assert CurrencyRate.objects.filter(currency='USD').count() == 5

    # scrap same page once more
    scraper.scrap_page('link')
    assert CurrencyRate.objects.count() == 5
    assert CurrencyRate.objects.filter(currency='USD').count() == 5

from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter

from exchange.views import CurrenciesApiViewSet


router = SimpleRouter()
router.register('api/currencies', CurrenciesApiViewSet, basename='currencies')

urlpatterns = [
    path('admin/', admin.site.urls),
] + router.urls


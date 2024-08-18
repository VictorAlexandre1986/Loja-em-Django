from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VendaViewSet, VendaRelatorioView

router = DefaultRouter()
router.register(r'vendas', VendaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('relatorio/', VendaRelatorioView.as_view(), name='relatorio_vendas'),
]
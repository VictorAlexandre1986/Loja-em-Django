from django.shortcuts import render

from rest_framework import viewsets
from .models import ItemVenda
from .serializers import ItemVendaSerializer

class ItemVendaViewSet(viewsets.ModelViewSet):
    queryset = ItemVenda.objects.all()
    serializer_class = ItemVendaSerializer

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Vendedor
from .serializers import VendedorSerializer

class VendedorViewSet(viewsets.ModelViewSet):
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer
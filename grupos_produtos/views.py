from django.shortcuts import render
from rest_framework import viewsets
from .models import GrupoProduto
from .serializers import GrupoProdutoSerializer

class GrupoViewSet(viewsets.ModelViewSet):
    queryset = GrupoProduto.objects.all()
    serializer_class = GrupoProdutoSerializer
from rest_framework import serializers
from .models import GrupoProduto

class GrupoProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrupoProduto
        fields = '__all__'

from rest_framework import serializers
from .models import Venda
from itens_venda.serializers import ItemVendaSerializer

class VendaSerializer(serializers.ModelSerializer):
    itens = ItemVendaSerializer(many=True, read_only=True)

    class Meta:
        model = Venda
        fields = '__all__'

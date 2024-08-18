from django.db import models
from grupos_produtos.models import GrupoProduto

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    grupo = models.ForeignKey(GrupoProduto, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
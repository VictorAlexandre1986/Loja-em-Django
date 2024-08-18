from django.test import TestCase

from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from .models import Venda, Cliente, Vendedor
from produtos.models import Produto
from itens_venda.models import ItemVenda
from grupos_produtos.models import GrupoProduto


class VendaRelatorioTestCase(APITestCase):
    def setUp(self):
        # Configurando dados de teste
        self.cliente = Cliente.objects.create(nome="Cliente Teste", email="cliente@teste.com")
        self.vendedor = Vendedor.objects.create(nome="Vendedor Teste", email="vendedor@teste.com")
        grupo = GrupoProduto.objects.create(nome="Grupo Teste")

        # Agora associe o grupo ao criar o Produto
        self.produto = Produto.objects.create(nome="Produto Teste", preco=100.0, grupo=grupo)  # Associe o produto ao grupo criado

        self.venda = Venda.objects.create(cliente=self.cliente, vendedor=self.vendedor)
        ItemVenda.objects.create(venda=self.venda, produto=self.produto, quantidade=2, preco_unitario=100.0)

        self.client = APIClient()

    def test_gera_relatorio_pdf(self):
        url = reverse('relatorio_vendas')  # Nome que definimos no urls.py
        params = {
            'data_inicio': '2024-08-16',
            'data_fim': '2024-08-31',
            'export': 'pdf'
        }
        response = self.client.get(url, params)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response['Content-Type'], 'application/pdf')

        # Verificar se o PDF não está vazio
        self.assertTrue(len(response.content) > 0)

        # Opcional: Salvar o PDF para inspeção manual (descomente se necessário)
        # with open('output.pdf', 'wb') as f:
        #     f.write(response.content)

    # Teste para geração de Excel (se implementado)
    def test_gera_relatorio_excel(self):
        url = reverse('relatorio_vendas')
        params={
         'export':'excel'
        }
        response = self.client.get(url, params)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response['Content-Type'], 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        self.assertTrue(len(response.content) > 0)


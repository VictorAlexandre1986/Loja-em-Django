from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from .models import Cliente

class ClienteCRUDTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.cliente_data = {'nome': 'Cliente Teste', 'email': 'cliente@teste.com'}
        self.cliente = Cliente.objects.create(**self.cliente_data)
        self.url = reverse('cliente-list')  # Certifique-se de que o nome 'cliente-list' está definido em urls.py

    def test_create_cliente(self):
        response = self.client.post(self.url, {'nome': 'Novo Cliente', 'email': 'novo@cliente.com', 'telefone':'12996653232'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cliente.objects.count(), 2)
        self.assertEqual(Cliente.objects.get(id=response.data['id']).nome, 'Novo Cliente')

    def test_read_cliente_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Apenas um cliente criado no setup

    def test_read_single_cliente(self):
        response = self.client.get(reverse('cliente-detail', kwargs={'pk': self.cliente.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], self.cliente.nome)

    def test_update_cliente(self):
        updated_data = {'nome': 'Cliente Atualizado', 'email': 'atualizado@cliente.com', 'telefone': '1296965241'}
        response = self.client.put(reverse('cliente-detail', kwargs={'pk': self.cliente.id}), updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.cliente.refresh_from_db()
        self.assertEqual(self.cliente.nome, 'Cliente Atualizado')

    def test_delete_cliente(self):
        response = self.client.delete(reverse('cliente-detail', kwargs={'pk': self.cliente.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Cliente.objects.count(), 0)

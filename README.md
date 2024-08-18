# API de uma loja em Django

## Tecnologias utilizadas 💻
<ul>
  <li>Python</li>
  <li>Django</li>
  <li>Sqlite</li>
</ul>

## Instalar as dependencias
```
pip install -r requirements.txt
```

## Migração no banco em caso de alterações
```
python manage.py makemigrations
```
```
python manage.py migrate
```

## Rodar o servidor
```
python manage.py runserver
```

## Acessar relatórios

### PDF
```
http://127.0.0.1:8000/api/vendas/relatorio/?data_inicio=2024-08-16&data_fim=2024-08-31&export=pdf
```

### Excel

```
http://127.0.0.1:8000/api/vendas/relatorio/?data_inicio=2024-08-16&data_fim=2024-08-31&export=excel
```

## Testes
### Testar os relatórios em pdf e excel
```
python manage.py test vendas.tests.VendaRelatorioTestCase
```

### Testar o crud das rotas de cliente
```
python manage.py test clientes.tests.ClienteCRUDTestCase
```

## Para acessar a documentação
```
http://127.0.0.1:8000/swagger/
```
```
http://127.0.0.1:8000/redoc/
```

## Para futuras atualizações
<p>git branch -M main
<p>git remote add origin https://github.com/VictorAlexandre1986/Loja-em-Django.git</p>
<p>git push -u origin main</p>

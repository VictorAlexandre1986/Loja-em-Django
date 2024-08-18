# Generated by Django 5.0.4 on 2024-08-16 18:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('grupos_produtos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grupos_produtos.grupoproduto')),
            ],
        ),
    ]

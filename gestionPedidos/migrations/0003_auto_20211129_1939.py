# Generated by Django 2.2.3 on 2021-11-30 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0002_auto_20211129_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulos',
            name='precio',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]

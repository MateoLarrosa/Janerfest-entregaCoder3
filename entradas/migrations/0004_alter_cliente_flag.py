# Generated by Django 4.2 on 2023-05-18 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entradas', '0003_cliente_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='flag',
            field=models.BooleanField(default=False),
        ),
    ]

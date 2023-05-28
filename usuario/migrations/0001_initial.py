# Generated by Django 4.2 on 2023-05-27 20:19

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoExtra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=20)),
                ('apellido', models.TextField(max_length=20)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatares')),
                ('mail', models.EmailField(max_length=254)),
                ('link_a_pagina', models.URLField(max_length=400)),
                ('descripcion', ckeditor.fields.RichTextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='infoextra', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

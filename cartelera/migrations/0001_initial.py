# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 18:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pelicula', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cartelera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
            ],
            options={
                'verbose_name': 'Cartelera',
                'verbose_name_plural': 'Carteleras',
            },
        ),
        migrations.CreateModel(
            name='Cine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Cine')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='cines/', verbose_name='Imagen')),
                ('direccion', models.CharField(max_length=150, verbose_name='Dirección')),
            ],
            options={
                'verbose_name': 'Cine',
                'verbose_name_plural': 'Cines',
            },
        ),
        migrations.AddField(
            model_name='cartelera',
            name='cine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cartelera.Cine'),
        ),
        migrations.AddField(
            model_name='cartelera',
            name='pelicula',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pelicula.Pelicula'),
        ),
    ]

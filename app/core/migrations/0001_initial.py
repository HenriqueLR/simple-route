# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maps',
            fields=[
                ('id_map', models.AutoField(serialize=False, verbose_name='Cod Mapa', primary_key=True, db_column=b'id_map')),
                ('name_map', models.CharField(unique=True, max_length=200, verbose_name='Nome', db_column=b'name_map')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de cria\xe7\xe3o', db_column=b'date_created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em', db_column=b'updated_at')),
                ('description_map', models.TextField(default=b'', null=True, verbose_name='Descri\xe7\xe3o', db_column=b'description', blank=True)),
            ],
            options={
                'ordering': ['id_map'],
                'db_table': 'maps',
                'verbose_name': 'map',
                'verbose_name_plural': 'maps',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Routes',
            fields=[
                ('id_route', models.AutoField(serialize=False, verbose_name='Cod Route', primary_key=True, db_column=b'id_route')),
                ('origin_route', models.CharField(max_length=200, verbose_name='Origem', db_column=b'origin_route')),
                ('destination_route', models.CharField(max_length=200, verbose_name='Destino', db_column=b'destination_route')),
                ('distance_route', models.CharField(max_length=200, verbose_name='Distancia', db_column=b'distance_route')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de cria\xe7\xe3o', db_column=b'date_created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em', db_column=b'updated_at')),
                ('description_route', models.TextField(default=b'', null=True, verbose_name='Descri\xe7\xe3o', db_column=b'description', blank=True)),
                ('id_map', models.ForeignKey(related_name='route_map', on_delete=django.db.models.deletion.PROTECT, verbose_name='Cod Map', to='core.Maps')),
            ],
            options={
                'ordering': ['id_route'],
                'db_table': 'routes',
                'verbose_name': 'route',
                'verbose_name_plural': 'routes',
            },
            bases=(models.Model,),
        ),
    ]

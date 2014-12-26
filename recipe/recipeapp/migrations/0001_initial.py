# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to=b'', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.FloatField()),
                ('units', models.CharField(default=b'C', max_length=1, choices=[(b'G', b'Gallons'), (b'C', b'Cups'), (b'T', b'Tbsp'), (b't', b'tsp'), (b'p', b'Pinch')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('directions', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to=b'', blank=True)),
                ('category', models.ForeignKey(to='recipeapp.Category')),
                ('ingredients', models.ManyToManyField(to='recipeapp.Ingredient')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

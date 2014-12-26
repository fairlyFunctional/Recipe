# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipeapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IngredientAmount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.FloatField()),
                ('units', models.CharField(max_length=1, choices=[(b'G', b'Gallons'), (b'C', b'Cups'), (b'T', b'Tbsp'), (b't', b'tsp'), (b'p', b'Pinch')])),
                ('name', models.ForeignKey(to='recipeapp.Ingredient')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='units',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(to='recipeapp.IngredientAmount'),
            preserve_default=True,
        ),
    ]

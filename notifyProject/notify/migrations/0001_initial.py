# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-15 21:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemId', models.BigIntegerField(db_column='itemid')),
                ('itemUrl', models.TextField(db_column='itemurl')),
                ('itemTitle', models.TextField(db_column='itemtitle')),
                ('isNew', models.BooleanField(db_column='isnew')),
            ],
            options={
                'db_table': 'news_item',
                'managed': False,
            },
        ),
    ]

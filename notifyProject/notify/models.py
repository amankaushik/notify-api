from __future__ import unicode_literals

from django.db import models

class NewsItem(models.Model):
    itemId = models.BigIntegerField(db_column='itemid')
    itemUrl = models.TextField(db_column='itemurl')
    itemTitle = models.TextField(db_column='itemtitle')
    isNew = models.BooleanField(db_column='isnew')
    class Meta:
        managed = False
        db_table = 'news_item'

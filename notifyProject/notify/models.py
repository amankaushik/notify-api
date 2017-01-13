from __future__ import unicode_literals

from django.db import models

class NewsItem(models.Model):
    itemId = models.BigIntegerField(db_column='itemid')
    itemUrl = models.TextField(db_column='itemurl')
    itemTitle = models.TextField(db_column='itemtitle')
    itemScore = models.BigIntegerField(db_column='score')
    itemTime = models.IntegerField(db_column='_time')
    isNew = models.BooleanField(db_column='isnew')
    class Meta:
        managed = True 
        db_table = 'news_item'

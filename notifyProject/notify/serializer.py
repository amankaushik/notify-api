'''
Serializers for notify-app
'''
from rest_framework import serializers
from notify.models import NewsItem

class NewsItemSerializer(serializers.ModelSerializer):
    '''
    Serializer for NewsItem model
    '''
    class Meta:
        '''
        Meta class for NewsItemSerializer
        '''
        model = NewsItem
        fields = ('itemId', 'itemUrl', 'itemTitle',\
                'itemScore', 'itemTime')

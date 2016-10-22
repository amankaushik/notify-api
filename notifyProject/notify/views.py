'''
Views
'''

from notify.models import NewsItem
from notify.serializer import NewsItemSerializer
from notify.implementation import HackerNewsAPIImpl
from rest_framework import generics
from django.http import HttpResponse

class NewsList(generics.ListCreateAPIView):
    HackerNewsAPIImpl()
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = NewsItem.objects.all()
    serializer_class = NewsItemSerializer
    http_method_names = ['get']

class NewsTop(generics.ListCreateAPIView):
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = NewsItem.objects.filter(isNew=True)
    serializer_class = NewsItemSerializer
    http_method_names = ['get']

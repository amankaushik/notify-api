from django.views.decorators.csrf import csrf_exempt
from models import NewsItem
from serializer import NewsItemSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from implementation import HackerNewsAPIImpl
from django.http import HttpResponse
from rest_framework import permissions
import json
import utils

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

def refreshNewsData(request):
    if request.method == 'GET':
        utils.refreshNewsData()
        return HttpResponse(json.dumps({'result': 'success'}), content_type='application/json')

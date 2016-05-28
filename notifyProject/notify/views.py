from django.views.decorators.csrf import csrf_exempt
from models import NewsItem
from serializer import NewsItemSerializer
from rest_framework.views import APIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from implementation import HackerNewsAPIImpl
import utils
from django.http import HttpResponse
import json

class NewsList(generics.ListCreateAPIView):
    HackerNewsAPIImpl()
    queryset = NewsItem.objects.all()
    serializer_class = NewsItemSerializer


class NewsTop(APIView):
    queryset = NewsItem.objects.filter(isNew=True)
    serializer_class = NewsItemSerializer

def refreshNewsData(request):
    if request.method == 'GET':
        utils.refreshNewsData()
        return HttpResponse(json.dumps({'result': 'success'}), content_type='application/json')

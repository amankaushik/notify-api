from django.views.decorators.csrf import csrf_exempt
from models import NewsItem
from serializer import NewsItemSerializer
from rest_framework.views import APIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics


class NewsList(generics.ListCreateAPIView):
    queryset = NewsItem.objects.all()
    serializer_class = NewsItemSerializer


class NewsTop(APIView):
    def get(sel, request):
        news = NewsTop.objects.filter(isNew=True)
        newsSerialized = NewsItemSerializer(news)
        return Response(newsSerialized.data)

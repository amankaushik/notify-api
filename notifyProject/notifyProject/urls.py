from django.conf.urls import url
from django.contrib import admin
from notify import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/notify/getall/$', views.NewsList.as_view()),
    url(r'^api/notify/getnew/$', views.NewsTop.as_view()),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.search, name='index'),
    path('base.html', views.base, name='base'),
    path('search.html', views.search, name='search'),
    path('result.html', views.result, name='result'),
]

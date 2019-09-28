from django.urls import path
from . import views

urlpatterns = [
    path('', views.search, name='index'),
    path('base', views.base, name='base'),
    path('search', views.search, name='search'),
    path('result', views.result, name='result'),
]

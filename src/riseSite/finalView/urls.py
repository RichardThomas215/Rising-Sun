from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home.html', views.contact, name='home'),
    path('base.html', views.base, name='base'),
    path('contact.html', views.contact, name='contact'),
    path('search.html', views.search, name='search'),
    path('result.html', views.result, name='result'),
]

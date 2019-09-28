from django.shortcuts import render

def index(req):
    return render(req, 'finalView/home.html')


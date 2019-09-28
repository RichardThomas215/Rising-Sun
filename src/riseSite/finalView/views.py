from django.shortcuts import render

def index(req):
    return render(req, 'finalView/home.html')

def search(req):
    return render(req, 'finalView/search.html')

def contact(req):
    return render(req, 'finalView/contact.html')

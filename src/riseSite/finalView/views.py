from django.shortcuts import render
from .models import *


def index(req):
    return render(req, 'finalView/home.html')

def base(req):
    return render(req, 'finalView/base.html')

def search(req):
    context_dict={}
    issues = Issue.objects.all()
    context_dict['issues']=issues
    return render(req, 'finalView/search.html', context_dict)

def contact(req):
    return render(req, 'finalView/contact.html')

def result(req):
    context_dict={}
    events = Event.objects.all()
    context_dict['events']=events
    return render(req, 'finalView/result.html', context_dict)

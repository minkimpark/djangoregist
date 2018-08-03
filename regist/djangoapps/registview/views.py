from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render


def registview(request):
    return render(request,'registview/registview.html')

def login(request):
    return render(request,'registview/login.html')

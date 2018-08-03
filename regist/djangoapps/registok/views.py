from django.shortcuts import render, redirect
from django.http import JsonResponse
from regist.models import *

def registok(request):

    id = request.POST['id']
    password = request.POST['password']
    name = request.POST['name']

    print(id)
    print(password)
    print(name)

    data = member(id=id,password=password,name=name)
    print(data)
    data.save()

    return JsonResponse({'return':'ok'})

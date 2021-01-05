from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import User
# Create your views here.
def helloWorld(request):
    return HttpResponse("Hello world")

@csrf_exempt
def signUp(request):
    data = json.loads(request.body)
    username = data['username']
    password = data['password']
    newUser = User(username=username, password=password)
    newUser.save()
    return HttpResponse('ok')
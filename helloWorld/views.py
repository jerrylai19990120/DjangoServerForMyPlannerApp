from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
import json
from .models import User
from .models import Task
import datetime
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

@csrf_exempt
def login(request):
    data = json.loads(request.body)
    username = data["username"]
    password = data["password"]

    with connection.cursor() as cursor:
        num = cursor.execute('SELECT * FROM helloWorld_user WHERE username = %s and password=%s', (username, password))
        if num == 0:
            return HttpResponse(json.dumps({"status": "not found"}), content_type="application/json")
        headers = [x[0] for x in cursor.description]
        result = dict(zip(headers, cursor.fetchone()))
    ret = json.dumps(result)

    return HttpResponse(ret, content_type="application/json")

@csrf_exempt
def addTask(request):
    data = json.loads(request.body)
    owner = data['owner']
    title = data['title']
    desc = data['desc']
    date = data['date']
    if data['finished']=='false':
        finished = False
    else:
        finished = True
    
    new_task = Task(owner=owner, title=title, desc=desc, date=date, finished=finished)
    new_task.save()

    return HttpResponse(json.dumps({"status": "added"}), content_type="application/json")

@csrf_exempt
def removeTask(request):

    data = json.loads(request.body)
    id = data['id']
    with connection.cursor() as cursor:
        num = cursor.execute('DELETE FROM helloWorld_task WHERE id=%s', [id])

    return HttpResponse(json.dumps({"deleted": f"{num}"}), content_type="application/json")

@csrf_exempt
def getTasks(request):
    data = json.loads(request.body)
    username = data['username']
    with connection.cursor() as cursor:
        num = cursor.execute('SELECT * FROM helloWorld_task WHERE owner=%s', [username])
        if num==0:
            return HttpResponse(json.dumps({"status": "failed"}), content_type="application/json")
        result = cursor.fetchall()
        headers = [x[0] for x in cursor.description]
        
        rets = []
        for i in result:
            temp = dict(zip(headers, i))
            rets.append(json.dumps(temp))
        
    return HttpResponse(rets, content_type="application/json")

@csrf_exempt
def updateTask(request):
    data = json.loads(request.body)
    id = data['id']
    if data['finished']=='false':
        finished = False
    else:
        finished = True

    with connection.cursor() as cursor:
        num = cursor.execute("UPDATE helloWorld_task SET finished=%r WHERE id=%s", [finished, id])
        if num==0:
            return HttpResponse(json.dumps({"updated": "false"}), content_type="application/json")
    
    return HttpResponse(json.dumps({"updated": "true"}), content_type="application/json")

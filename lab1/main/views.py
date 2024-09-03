from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Task, Comment

def index(request):
    cats = Category.objects.all()
    return render(request, 'main/index.html', {'cats': cats})

def cat_detail(request, cat_id):
    tasks = Task.objects.filter(category=cat_id)
    return render(request, 'main/cat_detail.html', {'tasks': tasks})

def task_detail(request, task_id):
    tasks = Task.objects.filter(id=task_id)
    return render(request, 'main/tasks.html', {'tasks': tasks})

def task_state(request, state):
    tasks = Task.objects.filter(statous=state)
    return render(request, 'main/tasks.html', {'tasks': tasks})

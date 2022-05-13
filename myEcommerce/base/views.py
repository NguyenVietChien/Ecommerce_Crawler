from django.shortcuts import render
from django.views.generic import View
from requests import request

# Create your views here.
from .models import Task
from .forms import TaskForm

class Ecommerce(View):
    def get(self, request):
        form = TaskForm()
        tasks = Task.objects.all()
        return render(request, 'task/main.html', context={'form': form, 'tasks': tasks})
# todo/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import newTaskForm  
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import TaskSerializer
from rest_framework.exceptions import NotFound

def home_redirect(request):
    if request.user.is_authenticated:
        return redirect('task_list')
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task_list')
    else:
        form = UserCreationForm()
    return render(request, 'todo/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('task_list')
    else:
        form = AuthenticationForm()
    return render(request, 'todo/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'todo/task_list.html', {'tasks': tasks})

@login_required
def task_form(request, pk=None):
    if pk:
        task = get_object_or_404(Task, pk=pk, user=request.user)
        form_title = "تعديل المهمة"
    else:
        task = None
        form_title = "إضافة مهمة جديدة"

    if request.method == 'POST':
        form = newTaskForm(request.POST, instance=task)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('task_list')
    else:
        form = newTaskForm(instance=task)
    
    return render(request, 'todo/task_form.html', {
        'form': form,
        'form_title': form_title,
        'task': task
    })

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.delete()
    return redirect('task_list')

# API Views
class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
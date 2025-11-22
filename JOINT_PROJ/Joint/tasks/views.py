from django.shortcuts import render, redirect
from .forms import NewTaskForm
from .models import Task
from django.shortcuts import get_object_or_404
# Create your views here.


def index(request):
    return render(request, template_name='index.html')

def show_tasks(request):
    tasks = Task.objects.all().order_by('datetime')
    print(tasks)
    return render(request, 'tasks.html', {
        'tasks': tasks
    })

def complete_task(request, task_id):
    tasks = get_object_or_404(Task, id=task_id)
    tasks.completed = True
    tasks.save()
    return redirect('tasks')

def add_task(request):

    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            priority = form.cleaned_data['priority']
            completed = form.cleaned_data['completed']
            task = Task(task=task, priority=priority, completed=completed)
            task.save()
            return redirect('tasks')

        return render(request, 'addtask.html', {'forms':form})
    return render(request, 'addtask.html', {'forms': NewTaskForm()})

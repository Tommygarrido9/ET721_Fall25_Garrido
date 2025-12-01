from django.shortcuts import render, redirect
from .models import Todolist
from .forms import Todolistform
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    todo_tasks = Todolist.objects.order_by('id')
    form = Todolistform()
    context = {'todo_tasks' : todo_tasks, 'form':form}
    return render(request, 'index.html', context)

@require_POST
def addTodoitem(request):
    form = Todolistform(request.POST)

    if form.is_valid():
        text = form.cleaned_data['text']
        Todolist.objects.create(text=text) 
        form.save()
    return redirect('index')

def completedToDo(request, todo_id):
    todo = Todolist.objects.get(pk = todo_id)
    todo.completed = True
    todo.save()
    return redirect('index')

def deletecompleted(request):
    Todolist.objects.filter(completed__exact = True).delete()
    return redirect('index')

def deleteall(request):
    Todolist.objects.all().delete()
    return redirect('index')
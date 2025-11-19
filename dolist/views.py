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
    print(request.POST['text'])
    if form.is_valid():
        new_todo = Todolist(text=request.POST['text'])
        new_todo.save()
    return redirect('index')
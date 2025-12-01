from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('add', views.addTodoitem, name = 'add'),
    path('completed/<todo_id>', views.completedToDo, name = 'completed'),
    path('deletecompleted', views.deletecompleted, name = 'deletecompleted'),
    path('deleteall', views.deleteall, name = 'deleteall'),
]
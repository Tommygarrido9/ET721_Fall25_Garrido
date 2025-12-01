from django.test import TestCase
from django.urls import reverse
from .models import Todolist
from .forms import Todolistform
from .views import addTodoitem
# Create tests here

class TodoviewstestTestCase(TestCase):
    def setUp(self):
        # create initial data
        self.task1 = Todolist.objects.create(text = "Task 1", completed = False)
        self.task2 = Todolist.objects.create(text = "Task 2", completed = False)
        self.task3 = Todolist.objects.create(text = "Task 3", completed = True)

    def test_index_view(self):
        # test the index view render the correct context and template
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_add_todo_item_view_valid_data(self):
        response = self.client.post(reverse(addTodoitem), {'text': 'Task 4'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Todolist.objects.count(), 4)
from django.test import TestCase
from django.urls import reverse
from dolist.models import Todolist
from dolist.forms import Todolistform
from dolist.views import addTodoitem, completedToDo, deletecompleted, deleteall
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
        self.assertEqual(Todolist.objects.filter(text='Task 4').exists())

    def test_completed_todo_view_valid_id(self):
        response = self.client.post(reverse(addTodoitem), {'text': 'New task', 'text': 'New task 2'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Todolist.objects.count(), 5)

    def test_add_todo_item_invalid(self):
        response = self.client.post(reverse(addTodoitem), {'text': ''})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Todolist.objects.count(), 3)

    def test_completed_todo_valid(self):
        response = self.client.post(reverse(completedToDo), args=[self.task1.id])
        self.assertEqual(response.status_code, 302)
        self.task1.refresh_from_db()
        self.assertTrue(self.task1.completed)
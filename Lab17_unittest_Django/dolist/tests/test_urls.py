from django.test import TestCase
from django.urls import reverse, resolve
from dolist.views import index, addTodoitem, completedToDo
from dolist.models import Todolist

class TestUrls(TestCase):
    def test_index_url(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)

    def test_add_url(self):
        url = reverse('add')
        self.assertEqual(resolve(url).func, addTodoitem)

    def test_completed_url(self):
        url = reverse("completed", args=[1])
        self.assertEqual(resolve(url).func, completedToDo)

    def test_urls_status_code(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('add'))
        self.assertEqual(response.status_code, 405)
        """
        response = self.client.get(reverse('completed', args=[1]))
        self.assertEqual(response.status_code, 302)
        """


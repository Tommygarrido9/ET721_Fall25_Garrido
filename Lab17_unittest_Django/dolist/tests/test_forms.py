from django.test import SimpleTestCase
from dolist.forms import Todolistform

class TodolistformTest(SimpleTestCase):
    def test_todo_list_form_valid_data(self):
        form = Todolistform(data = {'text': 'Buy groceries'})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['text'], 'Buy groceries')

    def test_todo_list_form_empty_data(self):
        form = Todolistform(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'], ['This field is required.'])

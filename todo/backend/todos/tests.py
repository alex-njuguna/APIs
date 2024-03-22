from django.test import TestCase

from .models import Todo


class TodoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # set up our data
        Todo.objects.create(title='first todo', body='first todo body')

    def test_title_content(self):
        # test title content
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.title}'
        self.assertEquals(expected_object_name, 'first todo')

    def test_body_content(self):
        # test body content is as expected
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.body}'
        self.assertEquals(expected_object_name, 'first todo body')

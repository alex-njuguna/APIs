from django.db import models

class Todo(models.Model):
    """representation of the todo table"""
    title = models.CharField(max_length=250)
    body = models.TextField()

    def __str__(self):
        return self.title

from django.views.generic import ListView

from .models import Book

class BookListView(ListView):
    """view to handle listing of all books"""
    model = Book
    template_name = 'book_list.html'

from rest_framework.generics import ListAPIView

from books.models import Book
from .serializers import BookSerializer

class BookAPIView(ListAPIView):
    """display a collection of books from an api"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer

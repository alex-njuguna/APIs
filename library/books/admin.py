from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    """customize the view of the Book model in the admin page"""
    list_display = ['id', 'title', 'subtitle', 'author', 'isbn']
    list_display_links = ['id', 'title']
    list_filter = ['author']
    list_per_page = 25

admin.site.register(Book, BookAdmin)

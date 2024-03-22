from django.contrib import admin

from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    # customize the Todo model viewing in the admin page
    list_display = ['id', 'title', 'body']
    list_display_links = ['id']
    list_filter = ['title']
    list_per_page = 25

admin.site.register(Todo, TodoAdmin)

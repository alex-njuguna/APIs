from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
    # customize post model view in the admin page
    list_display = ['id', 'author', 'title', 'body', 'created_at', 'updated_at']
    list_display_links = ['id', 'author', 'title']
    list_filter = ['author']
    list_per_page = 25

admin.site.register(Post, PostAdmin)

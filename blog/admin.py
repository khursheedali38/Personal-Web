from django.contrib import admin
from blog.models import Post
from django_markdown.admin import MarkdownModelAdmin

# Register your models here.
admin.site.register(Post, MarkdownModelAdmin)
from django.db import models
from django_markdown.models import MarkdownField

# Create your models here.
	
class Post(models.Model):
    category = models.CharField(max_length = 50)
    title = models.CharField(max_length = 100)
    overview = models.TextField()
    body = MarkdownField()
    date = models.DateTimeField()


    def __str__(self):
        return self.title

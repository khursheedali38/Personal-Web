from django.db import models

# Create your models here.
	
class Post(models.Model):
    category = models.CharField(max_length = 50)
    title = models.CharField(max_length = 100)
    overview = models.TextField()
    body = models.TextField()
    date = models.DateTimeField()


    def __str__(self):
        return self.title

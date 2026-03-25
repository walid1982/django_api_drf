from django.db import models

class Blog (models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.title

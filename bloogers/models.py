from django.db import models

class Blooger(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.title
class Comment(models.Model):
    blooger = models.ForeignKey(Blooger, on_delete=models.CASCADE, related_name='comments')
    comment_text = models.TextField()

    def __str__(self):
        return self.comment_text[:50]

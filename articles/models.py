from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    #add thumbnile
    #add author


def __str__(self):
    return self.title
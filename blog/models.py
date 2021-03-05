from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=250)
    image = models.ImageField(upload_to='blog/images/')
    url = models.URLField(blank=True)
    date = models.DateTimeField()

    def __str__(self):
        return self.title
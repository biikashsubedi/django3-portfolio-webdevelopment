from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/images/')
    time = models.DateField()

    def __str__(self):
        return self.title
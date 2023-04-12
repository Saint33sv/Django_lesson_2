from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    author_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

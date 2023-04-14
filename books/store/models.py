from django.db import models
from django.urls import reverse


class Book(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    author_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.id}) 

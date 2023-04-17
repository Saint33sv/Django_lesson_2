from django.db import models
from store.models import Book

class Image(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images')
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Картинки'
        verbose_name_plural = 'Картинки'
        ordering = ['title', 'book']

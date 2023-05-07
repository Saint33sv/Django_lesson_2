from django.db import models
from django.urls import reverse


class Book(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    author_name = models.CharField(max_length=50, verbose_name='Автор')
    price = models.DecimalField(max_digits=7, decimal_places=2, 
                                null=True, verbose_name='Цена')
    img = models.ImageField(upload_to='images', null=True, verbose_name='Фото')
    cat = models.ForeignKey('Category', 
                            on_delete=models.DO_NOTHING, 
                            null=True, verbose_name='Категории')
    slug = models.SlugField(max_length=100, unique=True, 
                            db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """возврат ссылки на конкретный обьект"""
        return reverse('post', kwargs={'book_slug': self.slug}) 

    class Meta:
        """отображение модели в админке"""
        verbose_name = 'Книги' # отобразить в админке модель Book как Книги
        verbose_name_plural = 'Книги' # Убрать символ 's' в конце названия модели
        ordering = ['-name', 'price'] # Сортиповка записей в модели


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория')
    slug = models.SlugField(max_length=100, unique=True, 
                            db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cat', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'

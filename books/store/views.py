from django.shortcuts import render
from django.conf import settings
from .models import Book


def books_page(request):
    books = Book.objects.all()
    data = [{'book': book.name, 
             'img': book.image_set.all().first().image,
             'price': book.price} for book in books]
    return render(request, 'index.html', {
        'data': data,
        'media_link': settings.MEDIA_URL,
        })

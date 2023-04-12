from django.shortcuts import render
from django.conf import settings
from .models import Book


def books_page(request):
    return render(request, 'index.html', {
        'books': Book.objects.all(),
        'media_link': settings.MEDIA_URL,
        })

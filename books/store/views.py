from django.shortcuts import render
from django.conf import settings
from .models import Book


def books_page(request):
    books = Book.objects.all()
    data = [{'book': book.name, 
             'img': book.image_set.all().first().image,
             'price': book.price,
             'url': book.get_absolute_url()} for book in books]
    menu = [
            {'title': 'О сайте', 'url_name': 'about'},
            {'title': 'Добавить книгу', 'url_name': 'add_book'},
            {'title': 'Обратная связь', 'url_name': 'contact'},
            {'title': 'Войти', 'url_name': 'login'},
            ]
    return render(request, 'index.html', {
        'data': data,
        'media_link': settings.MEDIA_URL,
        'menu': menu
        })

def about_page(request):
        return render(request, "about.html")


def add_book_page(request):
        return render(request, "add_book.html")


def contact_page(request):
        return render(request, "contact.html")


def login_page(request):
        return render(request, "login.html")


def get_post(request, book_id):
    book = Book.objects.get(id=book_id)
    data = {
            'name': book.name,
            'price': book.price,
            'post': book.description,
            'path': settings.MEDIA_URL,
            'img':  book.image_set.all().first().image
}
    return render(request, 'post.html', data)

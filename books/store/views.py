from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from .models import Book, Category
from .forms import AddBookForm


def books_page(request):
    books = Book.objects.all()
    data = [{'book': book.name, 
             'img': f"{settings.MEDIA_URL}{book.image_set.all().first().image}",
             'price': book.price,
             'url': book.get_absolute_url()} for book in books]
    return render(request, 'index.html', {'data': data})

def about_page(request):
        return render(request, "about.html")


def add_book_page(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            try:
                Book.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка добавления книги')
    else:
        form = AddBookForm()
    return render(request, "add_book.html", {
        'title': 'Добавить книку',
        'form': form,
        })


def contact_page(request):
        return render(request, "contact.html")


def login_page(request):
        return render(request, "login.html")


def get_post(request, book_slug):
    book = get_object_or_404(Book, slug=book_slug)
    data = {
            'name': book.name,
            'price': book.price,
            'post': book.description,
            'img':  f"{settings.MEDIA_URL}{book.image_set.all().first().image}",
    }
    return render(request, 'post.html', context=data)

def get_cats(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    books = Book.objects.filter(cat=category)
    data = [{'book': book.name, 
             'img': f"{settings.MEDIA_URL}{book.image_set.all().first().image}",
             'price': book.price,
             'url': book.get_absolute_url()} for book in books]
    return render(request, 'cats.html', {'data': data})

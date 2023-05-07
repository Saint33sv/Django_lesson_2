from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .models import Book
from .forms import AddBookForm


class BookHome(ListView):
    model = Book
    template_name = 'index.html'
    context_object_name = 'data'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context


#def books_page(request):
#    books = Book.objects.all()
#    data = []
#    for book in books:
#        if not book.image_set.all():
#            Image.objects.create(
        #                    title='error',
        #                    image="static_images/Oops.png",
        #                    book=book)
#            data.append({'book': book.name, 
                          #             'img': f"{settings.MEDIA_URL}{book.img}",
                          #             'price': book.price,
                          #             'url': book.get_absolute_url()})
#        else:
#            data.append({'book': book.name, 
                          #             'img': f"{settings.MEDIA_URL}{book.img}",
                          #             'price': book.price,
                          #             'url': book.get_absolute_url()})
#    return render(request, 'index.html', {'data': data,})

def about_page(request):
        return render(request, "about.html")



class AddBook(CreateView):
    """Обращение к класу формы и работа с ним"""
    form_class = AddBookForm
    template_name = 'add_book.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить книгу'
        return context

#def add_book_page(request):
#    if request.method == 'POST':
#        form = AddBookForm(request.POST, request.FILES)
#        if form.is_valid():
#            form.save()
#            return redirect('home')
#    else:
#        form = AddBookForm()
#    return render(request, "add_book.html", {
    #        'title': 'Добавить книку',
    #        'form': form,
    #        })


def contact_page(request):
        return render(request, "contact.html")


def login_page(request):
        return render(request, "login.html")


class PostBook(DetailView):
    model = Book
    template_name = 'post.html'
    context_object_name = 'data'
    slug_url_kwarg = 'book_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['data'].name
        return context

#def get_post(request, book_slug):
#    book = get_object_or_404(Book, slug=book_slug)
#    data = {
        #            'name': book.name,
        #            'price': book.price,
        #            'post': book.description,
        #            'img':  f"{settings.MEDIA_URL}{book.img}",
        #    }
#    return render(request, 'post.html', context=data)


class BookCategory(ListView):
    model = Book
    template_name = 'cats.html'
    context_object_name = 'data'
    allow_empty = False

    def get_queryset(self):
        return Book.objects.filter(cat__slug=self.kwargs['cat_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = str(context['data'][0].cat)
        return context

#def get_cats(request, cat_slug):
#    category = get_object_or_404(Category, slug=cat_slug)
#    books = Book.objects.filter(cat=category)
#    data = [{'book': book.name, 
              #             'img': f"{settings.MEDIA_URL}{book.img}",
              #             'price': book.price,
              #             'url': book.get_absolute_url()} for book in books]
#    return render(request, 'cats.html', {'data': data})

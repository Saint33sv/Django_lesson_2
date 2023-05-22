from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView

from .models import Book, Category
from .forms import AddBookForm, CreateUserForm, LoginUserForm, ContactForm
from .utils import DataMixin


class BookHome(DataMixin, ListView):
    model = Book
    template_name = 'index.html'
    context_object_name = 'data'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))


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



class AddBook(LoginRequiredMixin, DataMixin, CreateView):
    """Обращение к класу формы и работа с ним"""
    form_class = AddBookForm
    template_name = 'add_book.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить книгу")
        return dict(list(context.items()) + list(c_def.items()))

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


#def contact_page(request):
#        return render(request, "contact.html")


class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = "contact.html"
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Обратная связь')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')


class PostBook(DataMixin, DetailView):
    model = Book
    template_name = 'post.html'
    context_object_name = 'data'
    slug_url_kwarg = 'book_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['data'].name)
        return dict(list(context.items()) + list(c_def.items()))

#def get_post(request, book_slug):
#    book = get_object_or_404(Book, slug=book_slug)
#    data = {
        #            'name': book.name,
        #            'price': book.price,
        #            'post': book.description,
        #            'img':  f"{settings.MEDIA_URL}{book.img}",
        #    }
#    return render(request, 'post.html', context=data)


class BookCategory(DataMixin, ListView):
    model = Book
    template_name = 'cats.html'
    context_object_name = 'data'
    allow_empty = False

    def get_queryset(self):
        return Book.objects.filter(cat__slug=self.kwargs['cat_slug'
                                                         ]).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title=str(c.name),
                                      cat_selected=c.pk)
        return dict(list(context.items()) + list(c_def.items()))

#def get_cats(request, cat_slug):
#    category = get_object_or_404(Category, slug=cat_slug)
#    books = Book.objects.filter(cat=category)
#    data = [{'book': book.name, 
              #             'img': f"{settings.MEDIA_URL}{book.img}",
              #             'price': book.price,
              #             'url': book.get_absolute_url()} for book in books]
#    return render(request, 'cats.html', {'data': data})


class RegisterUser(DataMixin, CreateView):
    form_class = CreateUserForm
    template_name = "register.html"
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        """При регистрации автоматическая авторизация пользоватиля"""
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = "login.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        """После входа переходит на главную страницу"""
        return reverse_lazy('home')


def logout_user(request):
    """Выход зи учетной записи"""
    logout(request)
    return redirect('login')

from django.urls import path

from .views import *

urlpatterns = [
    path('', books_page, name='home'),
    path('post/<slug:book_slug>/', get_post, name="post"),
    path('cat/<slug:cat_slug>/', get_cats, name="cat"),
    path('about/', about_page, name="about"),
    path('add_book/', add_book_page, name="add_book"),
    path('contact/', contact_page, name="contact"),
    path('login/', login_page, name="login"),
]

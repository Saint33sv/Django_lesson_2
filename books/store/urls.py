from django.urls import path

from .views import *

urlpatterns = [
    path('', books_page, name='home'),
    path('post/<int:book_id>/', get_post, name="post"),
    path('about/', about_page, name="about"),
    path('add_book/', add_book_page, name="add_book"),
    path('contact/', contact_page, name="contact"),
    path('login/', login_page, name="login"),
]

from django.urls import path

from .views import *

urlpatterns = [
    path('', BookHome.as_view(), name='home'),
    path('post/<slug:book_slug>/', PostBook.as_view(), name="post"),
    path('cat/<slug:cat_slug>/', BookCategory.as_view(), name="cat"),
    path('about/', about_page, name="about"),
    path('add_book/', AddBook.as_view(), name="add_book"),
    path('contact/', contact_page, name="contact"),
    path('login/', LoginUser.as_view(), name="login"),
    path('logout/', logout_user, name="logout"),
    path('register/', RegisterUser.as_view(), name="register"),
]

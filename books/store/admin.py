from django.contrib import admin
from .models import *


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author_name', 'price') # Отображение полей для записей в модели
    list_display_links = ('id', 'name') # Выставит поле как ссылку на обьект
    search_fields = ('name', 'price') # Добавляет поле для поиска, ищит по указаным полям
    list_filter = ('name', 'price') # Фильтер по полям
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

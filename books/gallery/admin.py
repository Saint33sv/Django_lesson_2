from django.contrib import admin
from .models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'book', 'image') # Отображение полей для записей в модели
    list_display_links = ('id', 'title') # Выставит поле как ссылку на обьект
    search_fields = ('title', 'book') # Добавляет поле для поиска, ищит по указаным полям
    

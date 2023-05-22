from django.shortcuts import get_object_or_404
from django.db.models import Count

from .models import Category
from gallery.models import StatImage

menu = [
            {'title': 'О сайте', 'url_name': 'about'},
            {'title': 'Добавить книгу', 'url_name': 'add_book'},
            {'title': 'Обратная связь', 'url_name': 'contact'},
    ]

class DataMixin:
    paginate_by = 40
    """Вынос дублирования кода в классах представления в отдельный класс"""
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('book'))
        context['cats'] = cats
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu
        context['logo_img'] = get_object_or_404(StatImage, id=1).image
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context

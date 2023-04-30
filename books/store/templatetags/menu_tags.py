from django.shortcuts import get_object_or_404
from django import template
from django.conf import settings

from store.models import Category
from gallery.models import StatImage 


register = template.Library()

@register.inclusion_tag('head_menu.html')
def get_head_menu():
    menu = [
            {'title': 'О сайте', 'url_name': 'about'},
            {'title': 'Добавить книгу', 'url_name': 'add_book'},
            {'title': 'Обратная связь', 'url_name': 'contact'},
            {'title': 'Войти', 'url_name': 'login'},
    ]
    return {
            'menu': menu,
            'logo_img': 
            f"{settings.MEDIA_URL}{get_object_or_404(StatImage, id=1).image}"
            }


@register.inclusion_tag('side_bar_menu.html')
def get_side_bar():
    cats = Category.objects.all()
    data = [{
        'name': cat.name,
        'url': cat.get_absolute_url()
        } for cat in cats]
    return {
            'data': data,
            }

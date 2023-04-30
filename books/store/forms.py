from django import forms
from .models import *


class AddBookForm(forms.Form):
    name = forms.CharField(max_length=100, label='Название')
    slug = forms.SlugField(max_length=100, label='URL')
    description = forms.CharField(widget=forms.Textarea(attrs={
        'cols': 60, 
        'rows': 10
        }), label='Описание')
    author_name = forms.CharField(max_length=50, label='Автор')
    price = forms.DecimalField(max_digits=7, decimal_places=2, label='Цена')
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), 
                                 label='Категория', empty_label='Категория не выбрана')
    is_published = forms.BooleanField(required=False, initial=True,
                                      label='Опубликовано')
    

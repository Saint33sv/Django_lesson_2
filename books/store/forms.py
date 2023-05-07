from django import forms
from django.core.exceptions import ValidationError
from .models import *


class AddBookForm(forms.ModelForm):
    """Форма связаная с моделью"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Book
        fields = ['name', 'description', 'author_name', 'price', 'img', 'cat', 'slug']
        widgets = {
                'description': forms.Textarea(attrs={'cols': 60, 'rows': 10})
                }

    def clean_name(self):
        """Пример валидатора"""
        name = self.cleaned_data['name']
        if len(name) > 30:
            raise ValidationError('Длина превышает 30 символов')
        return name

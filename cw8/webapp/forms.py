from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, BaseValidator

from webapp.models import Product

def max_len_validator(string):
    if len(string) > 20:
        raise ValidationError('Заголовок должен быть длиннее 2 символов')
    return string

class CustomLenValidator(BaseValidator):
    def __init__(self, limit_value=20):
        message = 'Максимальная длина заголовка %(limit_value)s. Вы ввели %(show_value)s символов'
        super().__init__(limit_value=limit_value, message=message)

    def compare(self, value, limit_value):
        print(value)
        print(limit_value)
        return value > limit_value

    def clean(self, value):
        return len(value)


class ProductForm(forms.ModelForm):
    name = forms.CharField(
        validators=(MinLengthValidator(limit_value=2), CustomLenValidator()))

    class Meta:
        model = Product
        fields = ('name', 'category', 'description', 'picture')
        labels = {
            'name': 'название',
            'category': 'категория',
            'description': 'описание',
            'picture': 'изображение',
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 2:
            raise ValidationError('Заголовок должен быть длиннее 2 символов')
        if Product.objects.filter(name=name).exists():
            raise ValidationError('Заголовок с таким именем уже есть')
        return name

class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")

class FavoriteForm(forms.Form):
    note = forms.CharField(max_length=30, required=True, label='Заметка')
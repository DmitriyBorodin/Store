from django.core.exceptions import ValidationError
from django.forms import ModelForm

from catalog.models import Product


class CatalogForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'preview', 'category', 'price')

    def clean_name(self):
        name = self.cleaned_data['name']
        name_check = name.split()
        forbidden = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево',
                     'бесплатно', 'обман', 'полиция', 'радар']

        for word in name_check:
            if word in forbidden:
                raise ValidationError('Недопустимое название товара')

        return name


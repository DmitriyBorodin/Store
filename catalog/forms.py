from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField

from catalog.models import Product, Version


class StyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = "form-check-input"
            else:
                field.widget.attrs['class'] = "form-control"


class CatalogForm(StyleMixin, ModelForm):
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


class CatalogModeratorForm(StyleMixin, ModelForm):
    class Meta:
        model = Product
        fields = ('description', 'category', 'is_published')


class VersionForm(StyleMixin, ModelForm):
    class Meta:
        model = Version
        fields = "__all__"


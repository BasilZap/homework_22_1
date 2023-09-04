from django import forms
from products.models import Product, Version


BANNED_NAMES = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар')


# Класс миксин для стилизации форм
class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


# Класс генерации формы редактирования/добавления продукта
class ProductForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    # Метод валидации вводимого названия продукта
    def clean_product_name(self):
        cleaned_data = self.cleaned_data['product_name']

        for bad_word in BANNED_NAMES:
            if bad_word in cleaned_data.lower():
                raise forms.ValidationError(f'В названии в названии содержится слово {bad_word}, невозможно создать'
                                            f' продукт')

        return cleaned_data


# Класс генерации формы редактирования/добавления версии продукта
class VersionForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'
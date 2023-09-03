from django import forms
from products.models import Product, Version


BANNED_NAMES = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар')


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def clean_product_name(self):
        cleaned_data = self.cleaned_data['product_name']

        for bad_word in BANNED_NAMES:
            if bad_word in cleaned_data.lower():
                raise forms.ValidationError(f'В названии в названии содержится слово {bad_word}, невозможно создать'
                                            f' продукт')

        return cleaned_data


class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'
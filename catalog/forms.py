from django.core.exceptions import ValidationError
from django.forms import ModelForm
from catalog.models import Product


class ProductForm(ModelForm):
    forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название товара'
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание товара'
        })

        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Загрузите изображение'
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Выберете категорию'
        })

        self.fields['purchase_price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Укажите цену'
        })

        self.fields['created_at'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Дата создания'
        })

        self.fields['updated_at'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Дата последнего изменения'
        })

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name.lower() in self.forbidden_words:
            raise ValidationError(f'Запрещенные слова для названия продукта: {', '.join(self.forbidden_words)}')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if set(description.lower().split()).intersection(self.forbidden_words):
            raise ValidationError(f'Эти слова не должны присутствовать в описании: {', '.join(self.forbidden_words)}')
        return description

    def clean_purchase_price(self):
        purchase_price = self.cleaned_data.get('purchase_price')
        if purchase_price < 0:
            raise ValidationError('цена не может быть отрицательной')
        return purchase_price
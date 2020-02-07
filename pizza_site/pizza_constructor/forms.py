from django import forms
from django.forms import formset_factory, inlineformset_factory

from .models import Product


class ProductForm(forms.ModelForm):
    quantity = forms.IntegerField(min_value=0, widget=forms.NumberInput(), initial=0, label='Количество')
    category_id = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        widgets = {'name': forms.TextInput(attrs={'readonly': ''}),
                   # 'category': forms.TextInput(attrs={'readonly': ''}),
                   'price': forms.TextInput(attrs={'readonly': ''}),
                   'in_stock': forms.TextInput(attrs={'readonly': ''}),
                   }
        model = Product
        fields = ['name', 'in_stock', 'price']


class BaseProductFormset(forms.BaseFormSet):
    def get_prod_list(self):
        lst = list()
        for form in self.forms:
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            if quantity > 0:
                buffer = f'{quantity}-{name}({price})$'
                lst.append(buffer)
        res = ', '.join(lst)
        return res

    def get_total_price(self):
        res = 0
        for form in self.forms:
            res += form.cleaned_data['price'] * form.cleaned_data['quantity']
        return res


# ProductFormset = formset_factory(ProductForm, extra=0, formset=BaseProductFormset)
ProductFormset = formset_factory(ProductForm, extra=0)

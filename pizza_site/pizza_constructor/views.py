from django.shortcuts import render, redirect
from django.views import View

from .models import Product, Order
from .forms import ProductFormset


class HomeView(View):
    def get(self, request):
        products_list = Product.objects.order_by('id')
        formset = ProductFormset(initial=products_list.values())

        context = {
            'formset': formset,

        }
        return render(request, 'pizza_constructor/home.html', context)

    def post(self, request):
        pass
    #Добавить ПОСТ. нАстроить отображение формы заказа, создать для неё типлейт

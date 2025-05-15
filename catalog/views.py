# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render , get_object_or_404

from catalog.models import Product


def home(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "catalog/home.html", context)


def contacts(requests):
    return render(requests, template_name="catalog/contacts.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        return HttpResponse(f"Спасибо {name}! Сообщение получено")
    return render(request, "contacts.html")


def products_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "products_list.html", context)


def products_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'products_detail.html', context)

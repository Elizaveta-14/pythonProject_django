from django.views.generic import ListView,DetailView,CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from catalog.forms import ProductForm
from catalog.models import Product


class HomeListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'




class ContactsListView(ListView):
    model = Product
    template_name = 'catalog/contacts.html'


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'products'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ProductCreateView(CreateView,LoginRequiredMixin):
    model = Product
    fields = ['name', 'description', 'image', 'category', 'price']
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products_list')


    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(UpdateView,LoginRequiredMixin):
    model = Product
    fields = ['name', 'description', 'image', 'category', 'price']
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products_list')

    def get_success_url(self):
        return reverse('catalog:products_detail', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products_list')
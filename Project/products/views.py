from decimal import getcontext
#from msilib.schema import ListView
from turtle import title
from django.shortcuts import render
from django.template import context
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product
from django.db.models import Q
# Create your views here.


class ProductViewList(ListView):
    template_name = 'index.html'
    queryset = Product.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Listado de productos'
        context['products'] = context['product_list']
        return context


# Esta clase buscara un objeto mediante un identificador unico
class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProductSearchListView(ListView):
    template_name = 'products/search.html'

    def get_queryset(self):
        filters = Q(title__icontains=self.query()) | Q(
            category__title__icontains=self.query())
        return Product.objects.filter(filters)

    def query(self):
        return self.request.GET.get('q')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query()
        context['count'] = context['product_list'].count()
        return context

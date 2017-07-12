from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Product, Category

# Create your views here.

class ProductListView(generic.ListView):

    model = Product
    template_name = 'catalog/product_list.html'
    # Paginação
    # Automatica mente cria na url page = nume
    paginate_by = 2

product_list = ProductListView.as_view()

"""
def product_list(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'catalog/product_list.html', context)
"""
class CategoryListView(generic.ListView):

    template_name = 'catalog/category.html'
    paginate_by = 2

    def get_queryset(self):
        #category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Product.objects.filter(category__slug = self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context

category = CategoryListView.as_view()

"""
def category(request, slug):
    category = Category.objects.get(slug = slug)
    context = {
        'current_category': category ,
        'product_list': Product.objects.filter(category = category)
    }
    return render(request, 'catalog/category.html', context)
"""

def product(request, slug):
    product = Product.objects.get(slug= slug)
    context = {
        'product': product
    }

    return render(request , 'catalog/product.html', context)

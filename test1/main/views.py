from django.shortcuts import render, get_object_or_404
from .models import Category, Product

# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def product_list(request, category_slug=None):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    category = None
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request, 'main/Product/list.html',
                  {'category': category,
                  'categories': categories,
                  'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    related_product = Product.objects.filter(category=product.category,
                                             avaivlable=True).exclude(id=product.id)[:4]
    
    return render(request, 'main/Product/detail.html',{'product': product,
                                                       'related_product': related_product})
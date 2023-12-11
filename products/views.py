from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product


def all_products(request):
    """A view to show all produts, including sorting and search queries"""

    products = Product.objects.all()
    # so search_term context doesnt return error if no search
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didnt enter any search criteria!")
                return redirect(reverse('products'))
            
            # read django queries part of docs
            # i before contains makes it not case sensitive, double underscore here btw
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }
    
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """A view to show individual products in detail"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    
    return render(request, 'products/product_detail.html', context)

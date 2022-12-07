import random

from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, render, redirect

from apps.cart.cart import Cart
from apps.product.forms import AddToCartForm
from apps.product.models import Category, Product


def search(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))

    context = {
        'query': query,
        'products': products,
    }

    return render(request, 'product/search.html', context)


def product(request, category_slug, product_slug):
    cart = Cart(request)  # set a var for Cart instances

    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)

    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']  # a var for input data from AddToCart-form
            cart.add(product_id=product.id, quantity=quantity,
                     update_quantity=False)  # add the quantity of product (see line 27) to cart

            messages.success(request, 'Added to Cart')  # informing the user

            return redirect('product:product', category_slug=category_slug, product_slug=product_slug)
    else:
        form = AddToCartForm()

    similar_products = list(product.category.products.exclude(id=product.id))
    if len(similar_products) >= 4:
        similar_products = random.sample(similar_products, 4)

    context = {
        'product': product,
        'form': form,
        'similar_products': similar_products,
    }

    return render(request, 'product/product.html', context)


def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)

    context = {
        'category': category,
    }
    return render(request, 'product/category.html', context)

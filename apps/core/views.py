from django.shortcuts import render

from apps.product.models import Product


def frontpage(request):
    newest_products = Product.objects.all()[:8]

    context = {
        'newest_products': newest_products,
    }
    return render(request, 'core/frontpage.html', context)


def contact(request):
    return render(request, 'core/contact.html')

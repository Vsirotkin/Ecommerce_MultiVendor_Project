from django.shortcuts import render

def cart_detail(request):
    context = {}
    return render(request, 'cart/cart_detail.html', context)

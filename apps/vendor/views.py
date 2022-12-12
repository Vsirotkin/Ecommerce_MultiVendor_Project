from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render, get_object_or_404
from django.utils.text import slugify

from apps.vendor.forms import ProductForm
from apps.vendor.models import Vendor


def become_vendor(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)

            vendor = Vendor.objects.create(name=user.username, created_by=user)
            return redirect('core:frontpage')
    else:
        form = UserCreationForm()

    context = {
        'form': form,
    }
    return render(request, 'vendor/become_vendor.html', context)


@login_required
def vendor_admin(request):
    vendor = request.user.vendor
    products = vendor.products.all()
    orders = vendor.orders.all()

    for order in orders:
        order.vendor_amount = 0
        order.vendor_paid_amount = 0
        order.fully_paid = True

        for item in order.items.all():
            if item.vendor == request.user.vendor:
                if item.vendor_paid:
                    order.vendor_paid_amount += item.get_total_price()
            else:
                order.vendor_amount += item.get_total_price()
                order.fully_paid = False

    context = {
        'vendor': vendor,
        'products': products,
        'orders': orders,
    }

    return render(request, 'vendor/vendor_admin.html', context)


@login_required
def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = request.user.vendor
            product.slug = slugify(product.title)
            product.save()

            return redirect('vendor:vendor_admin')
    else:
        form = ProductForm()

    context = {
        'form': form,
    }
    return render(request, 'vendor/product_add.html', context)


@login_required()
def vendor_edit(request):
    vendor = request.user.vendor
    if request.method == 'POST':
        name = request.POST.get('name', )
        email = request.POST.get('email', )

        if name:
            vendor.created_by.email = email  # user's field email
            vendor.created_by.save()

            vendor.name = name
            vendor.save()

            return redirect('vendor:vendor_admin')

    context = {
        'vendor': vendor,
    }

    return render(request, 'vendor/vendor_edit.html', context)


def vendors(request):
    vendors = Vendor.objects.all()

    return render(request, 'vendor/vendors.html', {'vendors': vendors})


def vendor(request, vendor_id):
    vendor = get_object_or_404(Vendor, pk=vendor_id)

    return render(request, 'vendor/vendor.html', {'vendor': vendor})

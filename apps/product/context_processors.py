from apps.product.models import Category


def menu_categories(request):
    categories = Category.objects.all()

    context = {
        'menu_categories': categories
    }

    return context

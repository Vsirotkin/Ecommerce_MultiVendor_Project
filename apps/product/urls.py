from django.urls import path

from apps.product import views

app_name = 'product'
urlpatterns = [
    path('<slug:category_slug>/<slug:product_slug>/', views.product, name='product'),
    path('<category_slug>/', views.category, name='category'),
]

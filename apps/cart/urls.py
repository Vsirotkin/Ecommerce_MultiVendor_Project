from django.urls import path

from apps.cart import views

app_name = 'cart'
urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('success/', views.success, name='success'),
]

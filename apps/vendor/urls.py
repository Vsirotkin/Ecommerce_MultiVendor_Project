from django.urls import path

from apps.vendor import views

app_name = 'vendor'
urlpatterns = [
    path('become_vendor', views.become_vendor, name='become_vendor'),
    path('vendor_admin/', views.vendor_admin, name='vendor_admin'),
]

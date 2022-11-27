from django.urls import path

from apps.vendor import views

app_name = 'vendor'
urlpatterns = [
    path('become_vendor/', views.become_vendor, name='become-vendor'),
]

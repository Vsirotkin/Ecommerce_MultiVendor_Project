from django.contrib.auth import views as auth_views
from django.urls import path

from apps.vendor import views

app_name = 'vendor'
urlpatterns = [
    # app's views
    path('become_vendor/', views.become_vendor, name='become_vendor'),
    path('vendor_admin/', views.vendor_admin, name='vendor_admin'),
    # auth views
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='vendor/login.html'), name='login'),
]

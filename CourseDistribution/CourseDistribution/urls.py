"""CourseDistribution URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin-app/', include('MyAdmin.urls')),
    path('supplier-app/', include('Supplier.urls')),
    path('buyer-app/', include('Buyer.urls')),
    path('admin-register/', views.SignUp, name='register'),
    path('buyer-register/', views.SignUp_buyer, name='register_by'),
    path('supplier-register/', views.SignUp_supplier, name='register_su'),
    path('user-login/', views.login_sys, name='register'),
    path('logout/', views.logout_call, name='logout'),
    path('token' , views.token_send , name="token_send"),
    path('success' , views.success , name='success'),
    path('verify/<auth_token>' , views.verify , name="verify"),
    path('', views.homepage),
    path('accounts/', include('allauth.urls')),
]


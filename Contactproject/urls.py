"""
URL configuration for Contactproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from ContactApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home.as_view(),name='home_view'),
    path('reg',views.RegisterView.as_view(),name='reg_view'),
    path('log',views.UserLoginView.as_view(),name='log_view'),
    path('logout',views.UserLogoutView.as_view(),name='logout_view'),
    path('create',views.ContactCreateView.as_view(),name='create_view'),
    path('list',views.ContactListView.as_view(),name='list_view'),
    path('delete/<int:id>',views.ContactDeleteView.as_view(),name='delete_view'),
    path('update/<int:id>',views.ContactUpdateView.as_view(),name='update_view'),

 





]

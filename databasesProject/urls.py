"""
URL configuration for databasesProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from main import views
from main.views import MyLoginView, MyLogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('account', views.index, name='account'),
    path('shop', views.index, name='shop'),
    path('register', views.registerView, name='registerView'),
    path('my-courses', views.index, name='my-courses'),
    path('login/', MyLoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    path('api/get_user_data/', views.get_user_data, name='get_user_data'),
    path('api/register', views.register, name='register'),

]

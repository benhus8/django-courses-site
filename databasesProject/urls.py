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
from django.conf import settings #new
from django.conf.urls.static import static #new

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
    path('api/get_available_courses/', views.get_available_courses, name='get_available_courses'),
    path('api/register', views.register, name='register'),
    path('api/add_course_to_user/',views.add_course_to_user,name='add_course_to_user'),
    path('api/csrf_cookie/', views.get_csrf_token, name='get_csrf_token'),
    path('api/get_user_courses/',views.get_user_courses,name='get_user_courses'),
    path('api/get_course_subjects/<int:course_id>/',views.get_course_subjects,name='get_course_subjects'),
    path('api/get_course_title/<int:course_id>/',views.get_course_title,name='get_course_title'),
    path('api/delete_user_course/',views.delete_user_course,name='delete_user_course'),
    path('api/get_subject_lessons/<int:course_id>/<int:subject_id>/',views.get_subject_lessons,name='get_subject_lessons')

]

if settings.DEBUG:
    urlpatterns += static( settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
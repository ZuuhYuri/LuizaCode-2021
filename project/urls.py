"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
<<<<<<< Updated upstream
from app.views import form_empresas, home, form, create, view, edit, update, delete, form
=======
from app.views import form_empresas, home, form, create, view, edit, update, delete, create_empresas, view_empresas
>>>>>>> Stashed changes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('forms/', form, name='forms'),
    path('create/', create, name='create'),
    path('view/<int:pk>/', view, name='view'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),
<<<<<<< Updated upstream
    path('forms_empresa/', form_empresas, name='form_empresas'),
=======
    path('forms_empresa/', form_empresas, name='forms_empresas'),
    path('create_empresas/', create_empresas, name='create_empresas'),
    path('view_empresas/<int:pk>/', view_empresas, name='view_empresas'),
>>>>>>> Stashed changes


]

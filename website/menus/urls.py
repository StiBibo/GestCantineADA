"""
URL configuration for website project.

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
from django.urls import path
from . import views


app_name = 'menu'

urlpatterns = [
    path('', views.list_menu, name='list_menu'), 
    path('add_menu', views.add_menu, name='add_menu'), 
    path('update_menu/<int:id>', views.update_menu, name='update_menu'), 
    path('delete_menu/<int:id>', views.delete_menu, name='delete_menu'), 
    path('search', views.search_menu, name='search_menu'), 



]

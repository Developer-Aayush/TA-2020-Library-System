"""library_management_System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from library.views import *
from library import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login_view'),
    path('home', views.home, name="home"),
    path('add_book', views.addbooks, name="addBook"),
    path('update/<str:pk>/', views.update, name="up"),
    path('delete/<str:pk>/', views.delete, name="delete"),
    path('logout', views.logout_view, name="logoutView"),
    path('api', views.apiOverview, name="api-overview"),
    path('bookList', views.bookList, name="booklist"),
    path('bookDetail/<str:pk>', views.bookDetail, name="bookdetail"),
    path('bookCreate', views.bookCreate, name="bookcreate"),

    path('bookUpdate/<str:pk>', views.bookUpdate, name="bookupdate"),
    path('bookDelete/<str:pk>/', views.bookDelete, name="bookdelete"),
]

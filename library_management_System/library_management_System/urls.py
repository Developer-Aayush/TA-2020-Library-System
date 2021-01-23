
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

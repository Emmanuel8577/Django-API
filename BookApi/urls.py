from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('book-list', views.ShowAllBook, name='book-list'),
    path('book-detail/<int:pk>/', views.ViewBook, name='book-detail'),
    path('book-create/', views.CreateBook, name='book-create'),
    path('book-update/<int:pk>/', views.UpdateBook, name='book-update'),
    path('book-delete/<int:pk>/', views.DeleteBook, name='book-delete'),
    
]
from django.contrib import admin
from django.urls import path
from .views import( author_list, author_create, author_edit, author_delete,
                   book_list,book_create,book_edit,book_delete)


urlpatterns = [
    path('authors/', author_list, name='author_list'),
    path('authors/create', author_create, name='author_create'),
    path('authors/edit/<int:pk>', author_edit, name='author_edit'),
    path('authors/delete/<int:pk>', author_delete, name='author_delete'),
    path('books/', book_list, name='book_list'),
    path('books/create', book_create, name='book_create'),
    path('books/edit/<int:pk>', book_edit, name='book_edit'),
    path('books/delete/<int:pk>', book_delete, name='book_delete'),
    
]

# books/views.py

from django.views.generic import ListView, DetailView
from .models import Book
#from django.shortcuts import render


class BookListView(ListView):
    model= Book
    context_object_name = 'book_list'
    template_name='books/book_list.html'


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    
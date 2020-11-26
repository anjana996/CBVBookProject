from django.shortcuts import render
from books.models import Book
from django.views.generic import ListView,CreateView,DeleteView,DetailView,UpdateView
from django.urls import reverse_lazy
# Create your views here.
class ListBook(ListView):
    model = Book


class CreateBook(CreateView):
    model = Book
    fields = ["book_name","author","page","price"]
    success_url = reverse_lazy("list")

class ViewDetails(DetailView):
    model=Book
class DeleteBook(DeleteView):
    model=Book
    success_url = reverse_lazy("list")


class UpdateBook(UpdateView):
    model = Book
    fields = ["book_name","author","page","price"]
    template_name = "books/book_update.html"
    success_url = reverse_lazy("list")
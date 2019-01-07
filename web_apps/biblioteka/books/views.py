from django.shortcuts import render

# Create your views here.
from books.models import Book


def books_list(request):
    books = Book.objects.all()
    return render (
        template_name="books/books_list.html",
        context = {'books': books},
        request = request
    )
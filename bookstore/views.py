from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Book
# Create your views here.
# === Views ===
def index(request):
    context = {
        'book_list' : Book.objects.order_by('book_id')
    }
    return render(request, 'books.html', context)

def insert(request):
    context = {
        'book_id' : Book.objects.all().count() + 1
    }
    return render(request, 'insert.html', context)

def update(request):
    return render(request, 'update.html')

def delete(request):
    return render(request, 'delete.html')

# === APIs ===

def insert_api(request):
    book_id = request.POST['book-id']
    isbn = request.POST['isbn']
    name = request.POST['name']
    price = request.POST['price']
    author = request.POST['author']

    if(is_exist(book_id) == False):
        new_book(book_id, isbn, name, price, author)

    return HttpResponseRedirect(reverse('bookstore:insert'))

def update_api(request, book_id):
    book = Book.objects.get(book_id=int(book_id))
    isbn = request.POST['isbn']
    name = request.POST['name']
    price = request.POST['price']
    author = request.POST['author']
    book.isbn = isbn
    book.name = name
    book.price = price
    book.author = author
    book.save()
    return HttpResponseRedirect(reverse('bookstore:index'))

def delete_api(request, book_id):
    deleted_book = Book.objects.get(book_id=book_id)
    deleted_book.delete()
    return HttpResponseRedirect(reverse('bookstore:index'))

def new_book(book_id, isbn, name, price, author):
    book = Book(book_id=book_id, isbn=isbn, name=name, price=price, author=author)
    book.save()
    return book

def is_exist(book_id):
    books = Book.objects.all()
    for book in books:
        if(book.book_id == int(book_id)):
            return True
    return False

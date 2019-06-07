from django.shortcuts import render, redirect
from ..models import Book
from django.db import connection

# Create your views here.
cursor = connection.cursor()
def index(request):
    books = Book.objects.raw('Select * from crud_book')
    context = {'books': books}
    return render(request, 'crud/book/index.html', context)

def create(request):
    ISBN = request.POST['ISBN']
    name = request.POST['name']
    category = request.POST['category']
    cursor.execute('Insert into crud_book(ISBN, name, category) values(%s, %s, %s)', params=[ISBN, name, category] )
    return redirect('/crud/book')

def edit(request, id):
    book = Book.objects
    book.id = id
    
    context = {'book': book}
    return render(request, 'crud/book/edit.html', context)

def update(request, id):

    ISBN = request.POST['ISBN']
    name = request.POST['name']
    category = request.POST['category']
    cursor.execute("update crud_book set ISBN = %s, name = %s, category= %s where id = %s", params=[ISBN, name, category, id])
    return redirect('/crud/book')

def delete(request, id):
    cursor.execute("delete from crud_book where id=%s", params=[id])
    return redirect('/crud/book')

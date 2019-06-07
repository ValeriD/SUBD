from django.shortcuts import render, redirect
from ..models import Member, Book, BookMember
from django.db import connection

# Create your views here.
cursor = connection.cursor()
def index(request):
    members = Member.objects.raw('Select * from crud_member')
    context = {'members': members}
    return render(request, 'crud/member/index.html', context)

def create(request):
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    cursor.execute('Insert into crud_member(firstname, lastname) values(%s, %s)', params=[firstname, lastname] )
    return redirect('/crud/member')

def show(request, id):

    member = Member.objects.raw('Select * from crud_member where id=%s', params=[id])
    #member = Member.objects.raw('Select * from crud_member where id=%s', params=[id])
    books = Book.objects.raw('Select book.name, book.category from crud_bookmember inner join crud_book on crud_book.id=crud_bookmember.book where crud_bookmember.member = %s', params=[id])
    context = {'member': member,
                'books': books,
            }
    return render(request, 'crud/member/show.html/', context)

def edit(request, id):
    members = Member.objects
    members.id = id
    members.firstname = cursor.execute("Select firstname from crud_member where id=%s", params=[id])
    members.lastname = cursor.execute("Select lastname from crud_member where id=%s", params=[id])
    context = {'members': members}
    return render(request, 'crud/member/edit.html', context)

def update(request, id):
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    member = cursor.execute("update crud_member set firstname = %s, lastname = %s where id = %s", params=[firstname, lastname, id])
    return redirect('/crud/member')

def delete(request, id):
    cursor.execute("delete from crud_member where id=%s", params=[id])
    return redirect('/crud/member')
def add_book(request, id):
    book_id = request.POST['book_id']
    cursor.execute('insert into crud_bookmember(member_id, book_id) values(%s, %s)', params=[id, book_id])
    return redirect(show(None, id))

from django.shortcuts import render, redirect
from ..models import Member
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

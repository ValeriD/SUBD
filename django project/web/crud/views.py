from django.shortcuts import render, redirect
from .models import Member
from django.db import connection

# Create your views here.
cursor = connection.cursor()
def index(request):
    members = Member.objects.raw('Select * from crud_member')
    context = {'members': members}
    return render(request, 'crud/index.html', context)

def create(request):
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    #member = Member(firstname=request.POST['firstname'], lastname=request.POST['lastname'])
    #member.save()
    cursor.execute('Insert into crud_member(firstname, lastname) values(%s, %s)', params=[firstname, lastname] )
    return redirect('/')

def edit(request, id):
    members = cursor.execute("Select * from crud_member where id=%s", params=[id])
    #members = Member.objects.get(id=id)
    context = {'members': members}
    return render(request, 'crud/edit.html', context)

def update(request, id):

    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    cursor.execute("update crud_member set firstname = %s, lastname = %s ", params=[firstname, lastname])
    return redirect('/crud/')

def delete(request, id):
    member = Member.objects.get(id=id)
    member.delete()
    return redirect('/crud/')

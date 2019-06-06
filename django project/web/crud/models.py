from django.db import models

# Create your models here.

class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.name + " " + self.category

class Member(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)

    def __str__(self):
        return self.firstname + " " + self.lastname

class BookMember(models.Model):
    book = models.ForeignKey(Book,default=None)
    member = models.ForeignKey(Member,default=None)

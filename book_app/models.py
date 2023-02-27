from django.db import models

# Create your models here.

class Address(models.Model):
    number=models.PositiveIntegerField()
    street=models.CharField(max_length=50,blank=False,null=False)
    city=models.CharField(max_length=50,blank=False,null=False)
    state=models.CharField(max_length=50,blank=False,null=False)
    country=models.CharField(max_length=50,blank=False,null=False)
    postalCode=models.models.PositiveIntegerField(blank=False,null=False)

class Editor(models.Model):
    name=models.CharField(max_length=50,blank=False,null=False)
    email=models.EmailField(max_length=250)
    website=models.URLField(max_length=250)
    telephoneNumber=models.CharField(max_length=50,blank=False,null=False)
    address=models.OneToOneField(Address,on_delete=models.CASCADE)
class Book(models.Model):
    esbnCode=models.CharField(max_length=50,primary_key=True, default='00000000')
    title=models.CharField(max_length=50,blank=False,null=False)
    #5 digits for the whole number and 2 digits for the decimal
    price=models.models.DecimalField(max_digits=5, decimal_places=2)
    #default is the current date
    releaseDate=models.DateField(auto_now_add=True)
    #TextField for multiple lines
    summary=models.TextField(blank=True,null=True)
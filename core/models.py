from django.db import models
from django.contrib import admin
# Create your models here.

class Contactus(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=20)
    Company_name = models.CharField(max_length=15)
    Email = models.EmailField(max_length=25)
    Contact_no = models.CharField(max_length=10)
    Message=models.CharField(max_length=50)

    def __str__(self):
        """String for representing the Model object."""
        return self.Company_name
    class Meta:  
        db_table = "Contactus"

class ContactusAdmin(admin.ModelAdmin):
    list_display = ('id','Name','Company_name','Email','Contact_no','Message')

#this model is for shorting the companies 
class Company(models.Model):
    id = models.AutoField(primary_key=True)
    Company_name =  models.CharField(max_length=30)
    Company_img = models.ImageField(upload_to='media')

    def __str__(self):
        """String for representing the Model object."""
        return self.Company_name
    class Meta:  
        db_table = "Company"

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id','Company_name')


class Products(models.Model):
    id = models.AutoField(primary_key=True)
    Company_id = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True,blank=True)
    Item_name =  models.CharField(max_length=25)
    Item_img = models.ImageField(upload_to='media')
    Range = models.CharField(max_length=50,null=True,blank=True)
    Description = models.CharField(max_length=40,null=True,blank=True) 

    def __str__(self):
        """String for representing the Model object."""
        return self.Item_name
    class Meta:  
        db_table = "Products"

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id','Company_id','Item_name','Item_img','Range','Description')

#this brand model is for showing the images on the homepage...
class Brands(models.Model):
    id = models.AutoField(primary_key=True)
    Brand_name = models.CharField(max_length=30)
    Brand_img = models.ImageField(upload_to='media')

    def __str__(self):
        """String for representing the Model object."""
        return self.Brand_name
    class Meta:  
        db_table = "Brands"

class BrandsAdmin(admin.ModelAdmin):
    list_display = ('id','Brand_name','Brand_img')



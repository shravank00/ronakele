from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.utils import timezone
from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.core.exceptions import ValidationError
from .models import Brands,Products,Company,Contactus
# Create your views here.

def index(request):
    brands = Brands.objects.all()
    companys = Company.objects.all()
    return render(request,'index.html',{'brands':brands,'companys':companys})

def company(request):
    return render(request,'company.html')
    
def salesservice(request):
    return render(request,'Sales-Services.html')

def product(request):
    companys = Company.objects.all()

    return render(request,'Products.html',{'companys':companys})

def download(request):
    return render(request,'download.html')

def news(request):
    return render(request,'News.html')

def productdetails(request,id):
    pid = id
    product = Products.objects.get(id = pid)
    return render(request,'productdetails.html',{'product':product})

def contact(request):
    contactus = Contactus.objects.all()
    if request.method == "POST":
        name=request.POST["name"]
        email=request.POST["txtemail"]
        contact=request.POST["Contact"]
        company = request.POST["Company"]
        message = request.POST["Message"]
        contactus = Contactus(Name=name,Company_name=company,Email=email,Contact_no=contact,Message=message)
        contactus.save()
        return render(request,'Contact-Us.html')
    return render(request,'Contact-Us.html')

def Items(request,id):
    cid = id
    companys = Company.objects.all()
    products = Products.objects.filter(Company_id_id=cid)
   
    return render(request,'Items.html',{'products':products})
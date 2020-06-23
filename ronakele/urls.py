"""ronakele URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('index1',views.index,name='index1'),
    path('company',views.company,name='company'),
    path('salesservice',views.salesservice,name='salesservice'),
    path('Products',views.product,name='Products'),
    path('download',views.download,name='download'),
    path('news',views.news,name='news'),
    path('contactus',views.contact,name='contactus'),
    path('items/<int:id>',views.Items,name='items'),
    path('productdetails/<int:id>',views.productdetails,name='productdetails'),

]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

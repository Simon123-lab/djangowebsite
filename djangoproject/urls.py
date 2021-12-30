"""djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views
from inventory import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('test',views.checkuser),
    path('registeruser',views.register),
    path('',views.insertdata),
    path('viewcustomer',views.viewcustomer),
    path('prod_del/<int:id>',views.delete),
    path('search',views.search),
    path('insertproduct',views.insproduct)


    #path('',views.index),
    #path('customer',views.customer),
    #path('',include('inventory.urls'))
    #path('',views.checkuser)
]
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_STORE)
urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATICFILES_DIRS)

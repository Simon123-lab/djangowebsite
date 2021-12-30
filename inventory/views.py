from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.hashers import make_password,check_password

# Create your views here.

def insertdata(request):
   if request.method=='POST':
      namedata=request.POST['name']
      phonedata=request.POST['phone']
      addressdata=request.POST['address']
      customer_image=request.FILES['Image']


      customerdata=Customer.objects.create(name=namedata,phone=phonedata,address=addressdata,image_data=customer_image)



      customerdata.save()
      return render(request,'Customer.html',{"msg":"Data Inserted"})

   else:
      mydata=Customer.objects.all()
      return render(request,'Customer.html',{"data":mydata})

def checkuser(request):
   saud = Customer.objects.all().filter(name='zohaib')
   print(saud)
   return render(request, 'Customerdata.html')

def register(request):
   if request.method=='POST':
      username=request.POST['name']
      userpassword=request.POST['password']
      hashpassword=make_password(userpassword)
      userphone = request.POST['phone']
      userdata=Register.objects.create(user_name=username,user_password=hashpassword,user_phone=userphone)
      userdata.save()
      return render(request,'UserRegistration.html')


   else:
      return render(request,'UserRegistration.html')

def viewcustomer(request):
   mydata=Customer.objects.all()
   return render(request,'ViewCustomer.html',{"data":mydata})

def delete(request,id):
   mydata=Customer.objects.get(id=id)
   data=Customer.objects.all()
   #mydata.delete()
   #data=Customer.objects.all()


   #return render(request,'ViewCustomer.html',{"data":data})
   # mydata=Customer.objects.get(id=id)
   mydata.delete()
   return render(request,'ViewCustomer.html',{"data":data})

def search(request):
   if request.method=='POST':
      searchdata =request.POST['search']
      filterdata=Customer.objects.filter(name=searchdata)
      return render(request,'ViewCustomer.html',{"data":filterdata})
   else:
      mydata=Customer.objects.all()
      return render(request, 'ViewCustomer.html', {"data": mydata})

def insproduct(request):
   if request.method=='POST':
      productname=request.POST['name']
      productprice=request.POST['price']
      productdate = request.POST['date']
      fk_id=request.POST['mydata']
      fk_data=Category.objects.only('id').get(id=fk_id)
      prodadd=Product.objects.create(product_name=productname,product_price=productprice,expriy_date=productdate,fk_cat=fk_data)
      prodadd.save()
      #cat = Category.objects.all()
      messages.success(request,'data')
      return redirect('/insertproduct',{"msg":"data inserted"})
   else:
      cat=Category.objects.all()
      return render(request,'Productsinsert.html',{"data":cat})

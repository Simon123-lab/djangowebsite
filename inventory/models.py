from django.db import models

# Create your models here.
class Customer(models.Model):
    id=models.AutoField
    name=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    address=models.CharField(max_length=30)
    image_data=models.ImageField(upload_to='media')

class Category(models.Model):
    cat_id=models.AutoField
    name=models.CharField(max_length=20)

class Product(models.Model):
    pro_id=models.AutoField
    product_name=models.CharField(max_length=20)
    product_price=models.IntegerField()
    expriy_date=models.DateField()
    fk_cat=models.ForeignKey(Category,on_delete=models.CASCADE)

class Stock(models.Model):
    stock_id=models.AutoField
    quantity=models.IntegerField()
    fk_proid=models.ForeignKey(Product,on_delete=models.CASCADE)

class Orders(models.Model):
    or_id=models.AutoField
    or_amount=models.IntegerField(default=0)
    fk_custid=models.ForeignKey(Customer,on_delete=models.CASCADE)

class OrderList(models.Model):
    list_id=models.AutoField
    fk_order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    fk_product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)

class Register(models.Model):
    user_id=models.AutoField(primary_key=True)
    user_name=models.CharField(max_length=25)
    user_password=models.CharField(max_length=25)
    user_phone=models.CharField(max_length=25)



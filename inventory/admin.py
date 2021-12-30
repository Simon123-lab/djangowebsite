from django.contrib import admin
from .models import Customer
from .models import Category
from .models import Product
from .models import *

# Register your models here.
admin.site.register(Customer)
admin.site.register(Stock)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(OrderList)
admin.site.register(Register)

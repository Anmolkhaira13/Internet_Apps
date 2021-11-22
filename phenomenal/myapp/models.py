from django.db import models
import datetime
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
 name = models.CharField(max_length=200)
 warehouse = models.CharField(max_length=100 , default="Windsor")
 description = models.CharField(max_length=100, default="Windsor")
 def __str__(self):
  return "Category: "+self.name+" Warehouse: "+self.warehouse+" Info: "+self.description+"\n"


class Product(models.Model):
 category = models.ForeignKey(Category, related_name='products',on_delete=models.CASCADE)
 name = models.CharField(max_length=200)
 price = models.DecimalField(max_digits=10, decimal_places=2)
 stock = models.PositiveIntegerField(default=100)
 available = models.BooleanField(default=True)
 description= models.TextField(blank=True)
 interested = models.PositiveIntegerField(default=0)

 def __str__(self):
  return "product: "+self.name+" price: "+str(self.price)+" Stock: "+str(self.stock)+"\n"
 def refill(self):
  self.stock = self.stock+100



class Client(User):
 PROVINCE_CHOICES = [
 ('AB', 'Alberta'),
 ('MB', 'Manitoba'),
 ('ON', 'Ontario'),
 ('QC', 'Quebec'),]
 company = models.CharField(max_length=50, blank=True)
 shipping_address = models.CharField(max_length=300, null=True,
blank=True)
 city = models.CharField(max_length=20, default='Windsor')
 province=models.CharField(max_length=2, choices=PROVINCE_CHOICES,
default='ON')
 interested_in = models.ManyToManyField(Category)

 def __str__(self):
  return " name: "+self.first_name+" "+self.last_name+" Shipping Address: "+ self.shipping_address+"\n"

class Order(models.Model):
 ORDER_CHOICES = [(0, 'Order Cancelled'), (1, 'Order Placed'), (2, 'OrderShipped'),(3, 'Order Delivered')]
 product = models.ForeignKey(Product, on_delete=models.CASCADE)
 client = models.ForeignKey(Client, on_delete=models.CASCADE)
 num_units = models.PositiveIntegerField()
 order_status = models.IntegerField(choices=ORDER_CHOICES, default=1)
 status_date =  models.DateField()

 def __str__(self):
  return "Client name:"+ self.client.first_name+ "ordered product"+ self.product.name+" Quantity: "+ str(self.num_units)+"\n"
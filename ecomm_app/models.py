from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
class product(models.Model): # Model is base class
    CAT=((1,'mobile'),(2,'shoes'),(3,'clothes'))
    name=models.CharField(max_length=50 ,verbose_name="Product Name")
    price=models.FloatField()
    pdetails=models.CharField(max_length=100,verbose_name="Product Details")
    cat=models.IntegerField( verbose_name="Category", choices=CAT)  #category
    is_active=models.BooleanField(default=True, verbose_name="Available")
    pimage=models.ImageField(upload_to='image')


class cart(models.Model):
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column='uid')
    pid=models.ForeignKey(product,on_delete=models.CASCADE,db_column='pid')
    qty=models.IntegerField(default=1)

class order(models.Model):
    order_id=models.CharField(max_length=50)
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column='uid')
    pid=models.ForeignKey(product,on_delete=models.CASCADE,db_column='pid')
    qty=models.IntegerField(default=1)

# models.py


# class Payment(models.Model):
#     order_id = models.CharField(max_length=255)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     # Add other fields as needed

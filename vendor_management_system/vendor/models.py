from typing import Iterable
from django.db import models
import random
import string

# Create your models here.

# creating the model of the Vendors
class Vendors(models.Model):
    name=models.CharField(max_length=100)
    contact_details=models.TextField()
    address=models.TextField()
    vendor_code=models.CharField(max_length=20, unique=True, blank=True, editable=False)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    class meta:
        db_table="Vendors"

    def __str__(self) :
        return self.name
    

    def save(self,*args, **kwargs):
        if not self.vendor_code:
            self.vendor_code=self.generate_unique_vendor_code()
        return super().save(*args,**kwargs)
    

    def generate_unique_vendor_code(self):
        prefix="VEND"
        while True:
            code=prefix+"".join(random.choices(string.digits,k=6))
            if not Vendors.objects.filter(vendor_code=code).exists():
                return code

            

# model to create the purchase order
class PurchaseOrder(models.Model):
    STATUS_CHOICES = [
         ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
     ]


    po_number=models.CharField(max_length=100,unique=True)
    Vendors=models.ForeignKey(Vendors, on_delete=models.CASCADE)
    order_date=models.DateTimeField()
    delivery_date=models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    
    
    class meta:
        db_table="PurchaseOrder"

    
    def __str__(self):
        return self.po_number


from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name

    
class Product(models.Model):
    CATEGORY = (('Indoor','Indoor'),('Outdoor','Outdoor'))
    name = models.CharField(max_length=200,null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200,null=True,choices=CATEGORY)
    descripton = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name



class Order(models.Model):
    STATUS = (('Pending','Pending'),('Out for Delivery','Out for Delivery'),('Delivered','Delivered'))
    customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    product=models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    status = models.CharField(max_length=200,null=True,choices=STATUS)
    def __str__(self):
        return self.product.name

class ReelEntry(models.Model):
    TROLLEY_CHOICES = [(f'Trolley {i}', f'Trolley {i}') for i in range(1, 11)]
    ROW_CHOICES = [('Row {}'.format(i), 'ROW {}'.format(i)) for i in range(1, 6)]
    COL_CHOICES = [('Slot {}'.format(i), f'Slot {i}') for i in range(1, 51)]
    scanned_reel = models.CharField(max_length=23, null=True)
    quantity = models.FloatField(null=True)
    select_trolley_no = models.CharField(max_length=23, null=True, choices=TROLLEY_CHOICES)
    select_row_no = models.CharField(max_length=23, null=True, choices=ROW_CHOICES)
    select_slot_no = models.CharField(max_length=23, null=True, choices=COL_CHOICES)
    reel_no = models.CharField(max_length=10, null=True)
    bo_no = models.CharField(max_length=10, null=True)
    status = models.CharField(max_length=200, null=True,default='Empty')
    location = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.scanned_reel)

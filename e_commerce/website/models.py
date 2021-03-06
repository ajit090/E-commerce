from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.conf import settings
from django_countries.fields import CountryField


CATEGORY_CHOICES = (
    ('S', 'Shirt'),
    ('SW', 'Sport wear'),
    ('OW', 'Outwear')
)

# user model

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    customer_id  = models.CharField(max_length=50, blank=True, null=True) 

    def __str__(self):
        return self.user.username
        
#item model

class Item(models.Model):
    title = models.CharField(max_length=250)
    price = models.FloatField(max_length=50)
    dis_price = models.FloatField(max_length=50)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)

    def __str__(self):
        return self.title

# OrderItem model

class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    
    def __str__(self):
        return f"{self.quantity} of {self.item.title}"
# total amount
    def get_total_item_price(self):
        return self.quantity * self.item.price

# discount price amount
    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

# Final amount
    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()

#Order model
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    address = models.ForeignKey('Address',  on_delete=models.SET_NULL, blank=True, null=True)
    payment = models.ForeignKey('Payment', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total

# Address model
class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=100)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

        
# Payment model
class Payment(models.Model):
    charge_id = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created: 
        userprofile = UserProfile.objects.create(user=instance)

post_save.connect(userprofile_receiver, sender=settings.AUTH_USER_MODEL)
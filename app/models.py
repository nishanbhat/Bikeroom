from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.enums import Choices

STATE_CHOICES = (
    ('Bagmati', 'Bagmati'),
    ('Rapti', 'Rapti'),
    ('Lumbini', 'Lumbini'),
    ('Seti', 'Seti'),
    ('Sagarmatha', 'Sagarmatha'),
    ('Karnali', 'Karnali'),
    ('Mechi', 'Mechi'),
    ('Magakali', 'Magakali'),
    ('Koshi', 'Koshi'),
    ('Janakpur', 'Janakpur'),
    ('Gandaki', 'Gandaki'),
    ('Dhaulagiri', 'Dhaulagiri'),
    ('Bheri', 'Bheri'),
    ('Narayani', 'Narayani'),

)


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=50)

    def __str__(self):
        return str(self.id)


class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    product_image = models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)


STATUS_CHOICES = (

    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On the way', 'On the way'),
    ('Cancel', 'Cancel')

)


class Orderplaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=50, choices=STATE_CHOICES, default='Pending')

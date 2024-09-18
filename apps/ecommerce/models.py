from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

class Category(models.Model):
    name = models.CharField(max_length=100)
    products = models.ManyToManyField(Product, related_name='categories')  # Many-to-Many
    is_active = models.BooleanField(default=True)

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.TextField()
    products = models.ManyToManyField(Product, related_name='suppliers')  # Many-to-Many
    is_active = models.BooleanField(default=True)

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    order_date = models.DateField()
    status = models.CharField(max_length=50)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')  # One-to-Many
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')  # One-to-Many
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    orders = models.ManyToManyField(Order, related_name='customers')  # Many-to-Many
    is_active = models.BooleanField(default=True)

class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payments')  # One-to-Many
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    payment_method = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

class Shipment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='shipments')  # One-to-Many
    shipment_date = models.DateField()
    tracking_number = models.CharField(max_length=100)
    carrier = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')  # One-to-Many
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='reviews')  # One-to-Many
    rating = models.IntegerField()
    comment = models.TextField()
    is_active = models.BooleanField(default=True)

class Return(models.Model):
    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE, related_name='returns')  # One-to-Many
    return_date = models.DateField()
    reason = models.TextField()
    refund_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

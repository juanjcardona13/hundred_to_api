from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    nationality = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

class Book(models.Model):
    title = models.CharField(max_length=200)
    publish_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # One-to-Many
    is_active = models.BooleanField(default=True)

class Publisher(models.Model):
    name = models.CharField(max_length=150)
    country = models.CharField(max_length=50)
    established_year = models.IntegerField()
    is_active = models.BooleanField(default=True)

class Bookstore(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    publisher = models.ManyToManyField(Publisher)  # Many-to-Many
    is_active = models.BooleanField(default=True)

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)

class Order(models.Model):
    order_number = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  # One-to-Many
    order_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    is_active = models.BooleanField(default=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)  # One-to-Many
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # One-to-Many
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

class Employee(models.Model):
    name = models.CharField(max_length=100)
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

class Manager(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)  # One-to-One
    department = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

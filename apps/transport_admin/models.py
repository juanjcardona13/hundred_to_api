from django.db import models

# Create your models here.

class Vehicle(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE, related_name='vehicles')  # One-to-Many
    is_active = models.BooleanField(default=True)

class Owner(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)

class MaintenanceRecord(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='maintenance_records')  # One-to-Many
    service_date = models.DateField()
    description = models.TextField()
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    is_active = models.BooleanField(default=True)

class InsurancePolicy(models.Model):
    vehicle = models.OneToOneField(Vehicle, on_delete=models.CASCADE, related_name='insurance_policy')  # One-to-One
    policy_number = models.CharField(max_length=50)
    coverage_amount = models.DecimalField(max_digits=10, decimal_places=2)
    expiry_date = models.DateField()
    is_active = models.BooleanField(default=True)

class Trip(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='trips')  # One-to-Many
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    destination = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

class Driver(models.Model):
    name = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50)
    vehicles = models.ManyToManyField(Vehicle, related_name='drivers')  # Many-to-Many
    is_active = models.BooleanField(default=True)

class TrafficViolation(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='violations')  # One-to-Many
    violation_date = models.DateField()
    description = models.TextField()
    fine_amount = models.DecimalField(max_digits=8, decimal_places=2)
    is_active = models.BooleanField(default=True)

class FuelTransaction(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='fuel_transactions')  # One-to-Many
    transaction_date = models.DateField()
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    liters = models.DecimalField(max_digits=6, decimal_places=2)
    is_active = models.BooleanField(default=True)

class ServiceCenter(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=150)
    services_offered = models.TextField()
    is_active = models.BooleanField(default=True)

class Appointment(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='appointments')  # One-to-Many
    service_center = models.ForeignKey(ServiceCenter, on_delete=models.CASCADE, related_name='appointments')  # One-to-Many
    appointment_date = models.DateTimeField()
    service_description = models.TextField()
    is_active = models.BooleanField(default=True)

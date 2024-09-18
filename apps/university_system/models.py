from django.db import models

# Create your models here.

class University(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=150)
    founded_year = models.IntegerField()
    is_active = models.BooleanField(default=True)

class Department(models.Model):
    name = models.CharField(max_length=100)
    university = models.ForeignKey(University, on_delete=models.CASCADE)  # One-to-Many
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

class Professor(models.Model):
    name = models.CharField(max_length=100)
    hire_date = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)  # One-to-Many
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)  # One-to-Many
    is_active = models.BooleanField(default=True)

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    enrollment_date = models.DateField()
    is_active = models.BooleanField(default=True)

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  # One-to-Many
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  # One-to-Many
    grade = models.DecimalField(max_digits=4, decimal_places=2)
    is_active = models.BooleanField(default=True)

class Club(models.Model):
    name = models.CharField(max_length=100)
    creation_date = models.DateField()
    university = models.ForeignKey(University, on_delete=models.CASCADE)  # One-to-Many
    members = models.ManyToManyField(Student)  # Many-to-Many
    is_active = models.BooleanField(default=True)

class Library(models.Model):
    name = models.CharField(max_length=100)
    university = models.ForeignKey(University, on_delete=models.CASCADE)  # One-to-Many
    books_count = models.IntegerField()
    is_active = models.BooleanField(default=True)

class BookCopy(models.Model):
    library = models.ForeignKey(Library, on_delete=models.CASCADE)  # One-to-Many
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13)
    is_active = models.BooleanField(default=True)

class Borrow(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  # One-to-Many
    book_copy = models.ForeignKey(BookCopy, on_delete=models.CASCADE)  # One-to-Many
    borrow_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

class Attendee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    events = models.ManyToManyField(Event, related_name='attendees')  # Many-to-Many
    is_active = models.BooleanField(default=True)

class Speaker(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField()
    events = models.ManyToManyField(Event, related_name='speakers')  # Many-to-Many
    is_active = models.BooleanField(default=True)

class Session(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='sessions')  # One-to-Many
    title = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE, related_name='sessions')  # One-to-Many
    is_active = models.BooleanField(default=True)

class Sponsor(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.TextField()
    logo = models.ImageField(upload_to='sponsor_logos/')
    events = models.ManyToManyField(Event, related_name='sponsors')  # Many-to-Many
    is_active = models.BooleanField(default=True)

class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='tickets')  # One-to-Many
    attendee = models.ForeignKey(Attendee, on_delete=models.CASCADE, related_name='tickets')  # One-to-Many
    purchase_date = models.DateTimeField()
    ticket_type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

class Venue(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    capacity = models.IntegerField()
    events = models.ManyToManyField(Event, related_name='venues')  # Many-to-Many
    is_active = models.BooleanField(default=True)

class Feedback(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='feedbacks')  # One-to-Many
    attendee = models.ForeignKey(Attendee, on_delete=models.CASCADE, related_name='feedbacks')  # One-to-Many
    rating = models.IntegerField()
    comments = models.TextField()
    is_active = models.BooleanField(default=True)

class Organizer(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.TextField()
    events = models.ManyToManyField(Event, related_name='organizers')  # Many-to-Many
    is_active = models.BooleanField(default=True)

class Workshop(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='workshops')  # One-to-Many
    title = models.CharField(max_length=200)
    description = models.TextField()
    speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE, related_name='workshops')  # One-to-Many
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_active = models.BooleanField(default=True)

from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
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
    phone_number = models.CharField(max_length=15)
    events = models.ManyToManyField(Event, related_name='speakers')  # Many-to-Many
    is_active = models.BooleanField(default=True)

class Workshop(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='workshops')  # One-to-Many
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_active = models.BooleanField(default=True)

class Session(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE, related_name='sessions')  # One-to-Many
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_active = models.BooleanField(default=True)

class Feedback(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='feedbacks')  # One-to-Many
    attendee = models.ForeignKey(Attendee, on_delete=models.CASCADE, related_name='feedbacks')  # One-to-Many
    rating = models.IntegerField()
    comments = models.TextField()
    feedback_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

class Venue(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    capacity = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)

class EventVenue(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_venues')  # One-to-Many
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='event_venues')  # One-to-Many
    setup_date = models.DateTimeField()
    teardown_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

class Registration(models.Model):
    attendee = models.ForeignKey(Attendee, on_delete=models.CASCADE, related_name='registrations')  # One-to-Many
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrations')  # One-to-Many
    registration_date = models.DateTimeField()
    ticket_type = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

class Sponsorship(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='sponsorships')  # One-to-Many
    contact_info = models.TextField()
    is_active = models.BooleanField(default=True)

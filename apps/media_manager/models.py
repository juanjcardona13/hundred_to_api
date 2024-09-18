from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    birth_date = models.DateField()
    is_active = models.BooleanField(default=True)

class Album(models.Model):
    title = models.CharField(max_length=150)
    release_date = models.DateField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)  # One-to-Many
    is_active = models.BooleanField(default=True)

class Song(models.Model):
    title = models.CharField(max_length=150)
    duration = models.DurationField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE)  # One-to-Many
    is_active = models.BooleanField(default=True)

class Playlist(models.Model):
    name = models.CharField(max_length=100)
    creation_date = models.DateField()
    songs = models.ManyToManyField(Song)  # Many-to-Many
    is_active = models.BooleanField(default=True)

class Event(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=150)
    date = models.DateField()
    is_active = models.BooleanField(default=True)

class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)  # One-to-Many
    price = models.DecimalField(max_digits=8, decimal_places=2)
    seat_number = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)

class Attendee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    event = models.ManyToManyField(Event)  # Many-to-Many
    is_active = models.BooleanField(default=True)

class Movie(models.Model):
    title = models.CharField(max_length=150)
    release_year = models.IntegerField()
    is_active = models.BooleanField(default=True)

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)  # One-to-Many
    rating = models.IntegerField()
    comment = models.TextField()
    is_active = models.BooleanField(default=True)

class Director(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    movies = models.ManyToManyField(Movie)  # Many-to-Many
    is_active = models.BooleanField(default=True)

from django.db import models

# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    published = models.BooleanField(default=False)
    publish_date = models.DateTimeField(null=True, blank=True)
    last_modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=True)

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    published = models.BooleanField(default=False)
    publish_date = models.DateTimeField(null=True, blank=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category, related_name='posts')  # Many-to-Many
    tags = models.ManyToManyField(Tag, related_name='posts')  # Many-to-Many
    is_active = models.BooleanField(default=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')  # One-to-Many
    author_name = models.CharField(max_length=100)
    author_email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

class Media(models.Model):
    file = models.FileField(upload_to='media/')
    description = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True)
    is_active = models.BooleanField(default=True)

class Menu(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    items = models.ManyToManyField('MenuItem', related_name='menus')  # Many-to-Many
    is_active = models.BooleanField(default=True)

class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField()
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='sub_items')  # Self-Referential Many-to-One
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

class Setting(models.Model):
    key = models.CharField(max_length=255, unique=True)
    value = models.TextField()
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='blogs')  # One-to-Many
    is_active = models.BooleanField(default=True)

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField()
    profile_picture = models.ImageField(upload_to='author_pictures/')
    is_active = models.BooleanField(default=True)

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')  # One-to-Many
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='comments')  # One-to-Many
    content = models.TextField()
    published_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

class Tag(models.Model):
    name = models.CharField(max_length=50)
    blogs = models.ManyToManyField(Blog, related_name='tags')  # Many-to-Many
    is_active = models.BooleanField(default=True)

class Newsletter(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    sent_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

class Subscriber(models.Model):
    email = models.EmailField()
    subscription_date = models.DateTimeField()
    newsletters = models.ManyToManyField(Newsletter, related_name='subscribers')  # Many-to-Many
    is_active = models.BooleanField(default=True)

class Forum(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

class Post(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name='posts')  # One-to-Many
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')  # One-to-Many
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')  # One-to-Many
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='post_comments')  # One-to-Many
    content = models.TextField()
    published_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

class Like(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='likes', null=True)  # One-to-Many
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes', null=True)  # One-to-Many
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='likes')  # One-to-Many
    liked_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

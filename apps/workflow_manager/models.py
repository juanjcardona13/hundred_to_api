from django.db import models

# Create your models here.

class App(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='apps')  # One-to-Many
    is_active = models.BooleanField(default=True)

class DataSource(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=100)  # e.g., 'API', 'Database', 'File'
    configuration = models.JSONField()  # Store configuration details as JSON
    app = models.ForeignKey(App, on_delete=models.CASCADE, related_name='data_sources')  # One-to-Many
    is_active = models.BooleanField(default=True)

class DataField(models.Model):
    name = models.CharField(max_length=255)
    data_type = models.CharField(max_length=100)  # e.g., 'String', 'Number', 'Date'
    data_source = models.ForeignKey(DataSource, on_delete=models.CASCADE, related_name='fields')  # One-to-Many
    is_active = models.BooleanField(default=True)

class Workflow(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    trigger_event = models.CharField(max_length=100)  # e.g., 'Form Submission', 'Data Change'
    actions = models.JSONField()  # Store actions as JSON
    app = models.ForeignKey(App, on_delete=models.CASCADE, related_name='workflows')  # One-to-Many
    is_active = models.BooleanField(default=True)

class Form(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    fields = models.ManyToManyField(DataField, related_name='forms')  # Many-to-Many
    app = models.ForeignKey(App, on_delete=models.CASCADE, related_name='forms')  # One-to-Many
    is_active = models.BooleanField(default=True)

class FormSubmission(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE, related_name='submissions')  # One-to-Many
    submission_date = models.DateTimeField(auto_now_add=True)
    data = models.JSONField()  # Store submission data as JSON
    is_active = models.BooleanField(default=True)

class Page(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    app = models.ForeignKey(App, on_delete=models.CASCADE, related_name='pages')  # One-to-Many
    is_active = models.BooleanField(default=True)

class UserRole(models.Model):
    role_name = models.CharField(max_length=100)
    permissions = models.JSONField()  # Store permissions as JSON
    app = models.ForeignKey(App, on_delete=models.CASCADE, related_name='roles')  # One-to-Many
    is_active = models.BooleanField(default=True)

class Integration(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=100)  # e.g., 'Zapier', 'Webhooks'
    configuration = models.JSONField()  # Store configuration details as JSON
    app = models.ForeignKey(App, on_delete=models.CASCADE, related_name='integrations')  # One-to-Many
    is_active = models.BooleanField(default=True)

class Notification(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    send_date = models.DateTimeField()
    app = models.ForeignKey(App, on_delete=models.CASCADE, related_name='notifications')  # One-to-Many
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='notifications')  # One-to-Many
    is_active = models.BooleanField(default=True)

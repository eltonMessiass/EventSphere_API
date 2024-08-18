from django.db import models
from users.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Event(models.Model):
    STATUS_CHOICES = [
        ('scheduled','scheduled'),
        ('ongoing','ongoing'),
        ('completed', 'completed'),
        ('canceled', 'canceled'),
    ]
    name = models.CharField(max_length=255)
    descriptiom = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=255)
    organizers = models.ManyToManyField(User, related_name='organized_event')
    max_capacity = models.IntegerField()
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='scheduled')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='event_images', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    external_link = models.URLField(null=True, blank=True)
    is_private = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('Tag', related_name='events', blank=True)


    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

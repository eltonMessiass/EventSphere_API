from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import re
from django.core.validators import RegexValidator

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, max_length=30, blank=False, null=False)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)



    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['first_name', 'last_name','email']

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.email}'


class Profile(models.Model):
    role_choices = (
        ('ORG', 'Organizer'),
        ('PT', 'Participant')
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=5, choices=role_choices, default="PT")
    profile_picture = models.ImageField(upload_to='profile_pics', null=True, blank=True, default='foto_perfil.webp')
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(
        max_length=9,
        validators=[
            RegexValidator(
                regex=r'^8[2-7]\d{7}$',
                message="Invalid Phone number",
            )
        ]
    )



    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}  - {self.role}'


    
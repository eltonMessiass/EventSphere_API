from django.db import models
from users.models import User
from events.models import Event

# Create your models here.
class Enrollment(models.Model):
    STATUS_CHOICES = [
        ('confirmed', 'Confirmed'),
        ('pending', 'Pending'),
        ('canceled', 'Canceled'),
    ]
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    event = models.ForeignKey('events.Event', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    registration_date = models.DateTimeField(auto_now_add=True)
    ticket = models.OneToOneField('Ticket', on_delete=models.CASCADE, null=True, blank=True, related_name='enrollment_ticket')

    def __str__(self):
        return f'{self.user} - {self.event.name}'


class Ticket(models.Model):
    enrollment = models.OneToOneField(Enrollment, on_delete=models.CASCADE, related_name='assigned_ticket', null=True, blank=True)  # 'related_name' ajustado
    code = models.CharField(max_length=100, unique=True)
    issue_date = models.DateTimeField(auto_now_add=True)
    is_used = models.BooleanField(default=False)

    def __str__(self):
        return self.code

    
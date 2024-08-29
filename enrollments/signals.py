from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Enrollment, Ticket
import uuid





@receiver(post_save, sender=Enrollment)
def create_ticket(sender, instance, created, **kwargs):
    if created:
        ticket_code = str(uuid.uuid4()).replace('-', '').upper()[:10]
        Ticket.objects.create(enrollment=instance, code=ticket_code) 

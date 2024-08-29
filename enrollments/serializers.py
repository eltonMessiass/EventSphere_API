from rest_framework import generics, serializers
from .models import Enrollment, Ticket





class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['id', 'user', 'event', 'status', 'registration_date', 'ticket']


class  TicketSerializer(serializers.ModelSerializer);
    class Meta:
        model = Ticket
        fields = ['id', 'enrollment', 'code', 'issue_date', 'is_used']


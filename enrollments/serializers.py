from rest_framework import generics, serializers
from .models import Enrollment, Ticket





class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['id', 'user', 'event', 'status', 'registration_date', 'ticket']

    def create(self, validated_data):
        event = validated_data['event']
        if event.is_full():
            raise serializers.ValidationError('Event is full')
        return super().create(validated_data)



class  TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'enrollment', 'code', 'issue_date', 'is_used']


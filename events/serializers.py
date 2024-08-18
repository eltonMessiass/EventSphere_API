from rest_framework import serializers
from  .models import Event, Tag, Category


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['name', 'description', 'start_time', 'end_time', 'location', 'organizers', 'max_capacity', 'status', 'category', 'image', 'price', 'external_link', 'is_private', 'created_at', 'updated_at', 'tags'] 
    
    def validade_date(self, date):
        if date['start_time'] >= date['end_time']:
            raise serializers.ValidationError("The start date must be before the end date")
        return date
    
    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("The price cannot be negative")
        

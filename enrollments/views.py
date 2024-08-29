from django.shortcuts import render
from rest_framework import generics, status, permissions
from .models import Enrollment, Ticket
from events.models import Event
from .serializers import EnrollmentSerializer, TicketSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


# class EnrollmentLIST(generics.ListCreateAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     queryset = Enrollment.objects.all()
#     serializer_class = EnrollmentSerializer

class EnrollmentLIST(APIView):
    def post(self, request, format=None):
        serializer = EnrollmentSerializer(data=request.data)
        if serializer.is_valid():
            event = Event.objects.get(id=request.data.get('event'))
            if event.is_full():
                return Response({'error':'Event id full'}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class EnrollmentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer


class TicketLIST(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class TicketDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


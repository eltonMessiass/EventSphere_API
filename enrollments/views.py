from django.shortcuts import render
from rest_framework import generics, status, permissions
from .models import Enrollment, Ticket
from .serializers import EnrollmentSerializer
from rest_framework.views import APIView


class EnrollmentLIST(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class EnrollmentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer


class TicketLIST(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class =
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
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, format=None):
        serializer = EnrollmentSerializer(data=request.data)
        if serializer.is_valid():
            event = Event.objects.get(id=request.data.get('event'))
            if event.is_full():
                return Response({'error':'Event id full'}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def get(self, request, format=None):
        obj = Enrollment.objects.all()
        serializer = EnrollmentSerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        

class Enrolled_to_specific_Event(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, pk, format=None):
        data = Enrollment.objects.filter(event=pk)
        serializer = EnrollmentSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class EnrollmentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer


class TicketLIST(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
 

class TicketDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


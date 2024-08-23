from django.shortcuts import render, get_object_or_404
from .serializers import UserSerializer, ProfileSerilizer
from rest_framework.decorators import api_view, permission_classes
from .models import User, Profile
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny


@api_view(['POST', 'GET'])
@permission_classes([AllowAny])
def userView(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def user_detail(request, id):
    user = get_object_or_404(User, id=id)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def profileView(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerilizer(profiles, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET", "PUT"])
def profileDetailView(request, id):
    profile = get_object_or_404(Profile, id=id) 
    if request.method == "GET":
        serializer = ProfileSerilizer(profile)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = ProfileSerilizer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    

@api_view(["GET", "PUT"])
def logged_user_profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
        serializer = ProfileSerilizer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Profile.DoesNotExist:
        return Response({"error":"Profile not found"}, status=status.HTTP_404_NOT_FOUND)
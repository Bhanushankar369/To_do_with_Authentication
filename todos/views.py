from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer, TaskSerializer

from rest_framework.permissions import IsAuthenticated
from .models import Todo

from django.contrib.auth import authenticate

# Create your views here.

def index(request):
    return HttpResponse("Hii, Bhanu")


class RegisterView(APIView):
    permission_classes = []
    
    def post(self, request):
        serializer = RegisterSerializer(data = request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            
            # Creation of token
            token = Token.objects.create(user=user)
            
            return Response(
                {"token": token.key},
                status=status.HTTP_201_CREATED
            )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
class LoginView(APIView):
    permission_classes = []
    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username=username, password=password)
        
        
        if not user:
            return Response({"Error": "Invalid credentials"})
        
        token, created = Token.objects.get_or_create(user=user)
        
        return Response({
            "token": token.key
        })
        
class TaskToDo(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        serializer = TaskSerializer(data = request.data)
        
        if serializer.is_valid():
            task = serializer.save()
        
        return Response({"message": "Task Added"})
    
    
class GetTasks(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        tasks = Todo.objects.all()
        
        return Response({
            "tasks": [
                {
                    "task": t.task,
                    "description": t.description
                }
                for t in tasks
            ]})
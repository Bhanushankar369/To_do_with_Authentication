from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Todo

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ["username", "password"]
        
    def create(self, data):
        user = User.objects.create_user(
            username=data['username'],
            password=data['password']
        )
        
        return user
    
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["task", "description"]
        
    def create(self, data):
        todo = Todo.objects.create(
            task = data["task"],
            description = data["description"]
        )
        
        return todo
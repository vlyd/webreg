from rest_framework import serializers
from .models import CustomUser

class UsersSerializer(serializers.ModelSerializer ):
    class Meta:
        fields = ['id', 'username', 'email', 'score', 'level']
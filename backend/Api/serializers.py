from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

class User_serializer(ModelSerializer):
    class Meta:
        model=User
        fields=["id", "first_name", "last_name", "email", "password"]
from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.viewsets import ModelViewSet
from .serializers import User_serializer
from company.models import Company


class Login(ObtainAuthToken):
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES

class Signup(ModelViewSet):
    serializer_class=User_serializer
    queryset=Company.objects.all()


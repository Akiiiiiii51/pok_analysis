from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AppSerializer
from .models import App

# Create your views here.

class AppView(viewsets.ModelViewSet):
    serializer_class = AppSerializer
    queryset = App.objects.all()

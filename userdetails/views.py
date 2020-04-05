from django.shortcuts import render

# Create your views here.
from userdetails.models import users, ActivePeriod
from userdetails.serializers import usersSerializer, ActivePeriodSerializer
from rest_framework import viewsets

class usersViewSet(viewsets.ModelViewSet):
    queryset = users.objects.all()
    serializer_class = usersSerializer

class activeViewSet(viewsets.ModelViewSet):
    queryset = ActivePeriod.objects.all()
    serializer_class = ActivePeriodSerializer

from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .models import *
from .serializers import CharSerializer
from rest_framework import serializers

# Create your views here.
class CharList(generics.ListCreateAPIView):
	queryset = Characther.objects.all()
	serializer_class = CharSerializer
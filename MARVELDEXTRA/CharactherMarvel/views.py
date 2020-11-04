from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework import serializers

# Create your views here.
class CharList(generics.ListCreateAPIView):
	queryset = Characther.objects.all()
	serializer_class = CharSerializer


class ComicList(generics.ListCreateAPIView):
	queryset = Characther.objects.filter().values('name','comics')
	serializer_class = ComicSerializer
	

class EventsList(generics.ListCreateAPIView):
	queryset = Characther.objects.filter().values('name','events')
	serializer_class = EventsSerializer

class SeriesList(generics.ListCreateAPIView):
	queryset = Characther.objects.filter().values('name', 'series')
	serializer_class = SeriesSerializer

class StoryList(generics.ListCreateAPIView):
	queryset = Characther.objects.filter().values('name', 'stories')
	serializer_class = StorySerializer

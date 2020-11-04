from rest_framework.response import Response
from rest_framework import generics,status
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework import serializers

# Create your views here.
class CharList(generics.ListCreateAPIView):
	queryset = Characther.objects.all()
	serializer_class = CharSerializer

class IDCharList(generics.ListCreateAPIView):
	serializer_class = CharSerializer  
	
	def get_queryset(self):
		id = self.kwargs['id']
		return Characther.objects.filter(id=id)

class ComicList(generics.ListCreateAPIView):
	serializer_class = ComicSerializer

	def get_queryset(self):
		id = self.kwargs['id']
		return Characther.objects.filter(id=id).values('name','comics')

class EventsList(generics.ListCreateAPIView):
	serializer_class = EventsSerializer

	def get_queryset(self):
		id = self.kwargs['id']
		return Characther.objects.filter(id=id).values('name', 'events')

class SeriesList(generics.ListCreateAPIView):
	serializer_class = SeriesSerializer

	def get_queryset(self):
		id = self.kwargs['id']
		return Characther.objects.filter(id=id).values('name', 'series')

class StoryList(generics.ListCreateAPIView):
	serializer_class = StorySerializer

	def get_queryset(self):
		id = self.kwargs['id']
		return Characther.objects.filter(id=id).values('name', 'stories')

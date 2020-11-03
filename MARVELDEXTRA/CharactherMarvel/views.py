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

def get(self, request, id):
    id = request.GET.get('id', '')

    return render(request, self, {'comics': get_object_or_404(comics, pk = id)})

class ComicList(generics.ListCreateAPIView):
	queryset = Characther.objects.filter().values('name', 'comics')
	serializer_class = ComicSerializer

	


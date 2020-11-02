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


class ComicList(generics.ListCreateAPIView):
	queryset = Characther.objects.name + Characther.objects.comics
	serializer_class = CharSerializer

	
def get(self, request):
    id = request.GET.get('id', '')

    return render(request, self, {'comics': get_object_or_404(Comics, pk = id)})
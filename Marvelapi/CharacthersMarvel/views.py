from rest_framework import generics
from .serializers import *


# Create your views here.
class CharList(generics.ListCreateAPIView):
	queryset = Character.objects.all()
	serializer_class = CharSerializer

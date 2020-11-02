from rest_framework import serializers
from .models import *



class CharSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characther
        fields = ['id', 'name', 'comics', 'events','series', 'stories']


   


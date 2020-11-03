from rest_framework import serializers
from .models import *



class CharSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characther
        fields = ['id', 'name', 'comics', 'events','series', 'stories']


class ComicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characther
        fields = ['id', 'name', 'comics']


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characther
        fields = ['id', 'name', 'events']

class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characther
        fields = ['id', 'name', 'series']

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Characther
        fields = ['id', 'name', 'stories']
from rest_framework import serializers
from .models import *

#criando o serializers

class CharSerializer(serializers.ModelSerializer):

    class Meta:
        model = Character
        fields = ['id', 'comics', 'events', 'series', 'stories']

class ComicSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comics
        fields = ['id', 'comics']

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'events']

class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ['id', 'series']

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Stories
        fields = ['id', 'stories']
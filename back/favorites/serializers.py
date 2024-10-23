from rest_framework import serializers
from .models import FavoriteEvents, ViewedEvents

class FavoriteEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteEvents
        fields = '__all__'

class ViewedEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewedEvents
        fields = '__all__'
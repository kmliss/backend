from rest_framework import viewsets
from .models import FavoriteEvents, ViewedEvents
from .serializers import FavoriteEventsSerializer, ViewedEventsSerializer

class FavoriteEventsViewSet(viewsets.ModelViewSet):
    queryset = FavoriteEvents.objects.all()
    serializer_class = FavoriteEventsSerializer

class ViewedEventsViewSet(viewsets.ModelViewSet):
    queryset = ViewedEvents.objects.all()
    serializer_class = ViewedEventsSerializer
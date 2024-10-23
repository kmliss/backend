from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FavoriteEventsViewSet, ViewedEventsViewSet

router = DefaultRouter()
router.register(r'favorite-events', FavoriteEventsViewSet)
router.register(r'viewed-events', ViewedEventsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
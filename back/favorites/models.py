from django.db import models
from django.utils import timezone
from accounts.models import Users
from events.models import Events

class FavoriteEvents(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    event_id = models.ForeignKey(Events, on_delete=models.CASCADE)
    added_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('user_id', 'event_id')

    def __str__(self):
        return f"{self.user_id.username} favorited {self.event_id.name} at {self.added_at}"
    
class ViewedEvents(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    event_id = models.ForeignKey(Events, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('user_id', 'event_id')

    def __str__(self):
        return f"{self.user_id.username} viewed {self.event_id.name} at {self.viewed_at}"

from django.db import models
from django.utils import timezone
from accounts.models import Users
from genres.models import Genres
from categories.models import Categories


class Events(models.Model):
    event_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    event_date = models.DateField()
    price = models.FloatField()
    organizer = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Tickets(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    event_id = models.ForeignKey(Events, on_delete=models.CASCADE)
    buyer_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    ticket_class = models.CharField(max_length=50)
    seat = models.CharField(max_length=50)

    def __str__(self):
        return f"Ticket {self.ticket_id} for {self.event_id.name}"
    
class EventGenres(models.Model):
    event_id = models.ForeignKey(Events, on_delete=models.CASCADE)
    genre_id = models.ForeignKey(Genres, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('event_id', 'genre_id')

    def __str__(self):
        return f"{self.event_id.name} - {self.genre_id.name}"

class EventCategories(models.Model):
    event_id = models.ForeignKey(Events, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('event_id', 'category_id')

    def __str__(self):
        return f"{self.event_id.name} - {self.category_id.name}"
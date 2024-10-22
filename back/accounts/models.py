from django.db import models
from genres.models import Genres
from categories.models import Categories

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password_hash = models.CharField(max_length=255)
    role = models.CharField(max_length=50, default='user')
    status = models.CharField(max_length=20, default='active')

    def __str__(self):
        return self.username

class UserFavoriteGenres(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    genre_id = models.ForeignKey(Genres, on_delete=models.CASCADE)
    preference_level = models.IntegerField(default=1)

    class Meta:
        unique_together = ('user_id', 'genre_id')

    def __str__(self):
        return f"{self.user_id.username} prefers {self.genre_id.name} (Level: {self.preference_level})"

class UserFavoriteCategories(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    preference_level = models.IntegerField(default=1)

    class Meta:
        unique_together = ('user_id', 'category_id')

    def __str__(self):
        return f"{self.user_id.username} prefers {self.category_id.name} (Level: {self.preference_level})"

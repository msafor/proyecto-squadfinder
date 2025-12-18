from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    gamertag= models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.gamertag
    
class Game(models.Model):
    nombre = models.CharField(max_length=100)
    slug= models.CharField(max_length=100, unique=True)
    cover_image = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nombre
    
class SquadRequest(models.Model):
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    rank_required = models.CharField(max_length=50)
    mic_required = models.BooleanField(default=False)
    descripcion= models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
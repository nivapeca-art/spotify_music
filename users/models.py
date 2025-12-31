from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class MusicPreference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='preferences')
    artist = models.CharField(max_length=100)
    top_tracks = models.JSONField()

    def __str__(self):
        return f"{self.user.name} - {self.artist}"


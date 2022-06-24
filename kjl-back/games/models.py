from django.db import models
from django.conf import settings

# Create your models here.
class Omok(models.Model):
    result = models.BooleanField()
    opp = models.CharField(max_length=20)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE )
    
class OneToFifty(models.Model):
    result = models.CharField(max_length=20)
    type = models.CharField(max_length=5)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE )

class SongQuiz(models.Model):
    result = models.CharField(max_length=20)
    type = models.CharField(max_length=5)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE )
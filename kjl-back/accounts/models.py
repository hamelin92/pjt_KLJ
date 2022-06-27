from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    nickname = models.CharField(max_length=10, unique=True)   
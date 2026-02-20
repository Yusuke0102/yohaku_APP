from django.db import models
from django.contrib.auth.models import AbstractUser

class AuthUser(AbstractUser):
    email = models.EmailField("email address", unique=True)
    birth_date = models.DateField(null=True, blank=True)
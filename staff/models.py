from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Crew(AbstractUser):
    salary = models.FloatField('Salário')    

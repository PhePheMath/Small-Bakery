from django.db import models

# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length=80)
    ingredients = models.ManyToManyField(to='food.Ingredient')

    def __str__(self):
        return f'{self.name.upper()}'

class Ingredient(models.Model):
    name = models.CharField('Nome do igrediente', max_length=80, unique=True)
    value_by_kilo = models.FloatField('Média de valor por quilo')
    
    def __str__(self):
        return self.name.upper()

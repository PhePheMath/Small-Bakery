from django.db import models

# Create your models here.

class Order(models.Model):
    customer = models.CharField('Cliente', max_length=80)
    value = models.FloatField('Valor de entrega')
    product = models.ForeignKey(to='food.Food', on_delete=models.CASCADE)
    address = models.CharField('Endereço', max_length=80)


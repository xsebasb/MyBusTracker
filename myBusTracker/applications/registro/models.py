from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Bus(models.Model):
    id = models.AutoField(primary_key = True)
    buses = models.CharField('Nombre bus:', max_length = 90, blank = False, null = False)
    descripcion = models.CharField('Descripción: ', max_length = 110, blank = False, null = False)


    class Meta:
        verbose_name = 'Bus'
        verbose_name_plural = 'Bus'

    def __str__(self):
        return self.buses

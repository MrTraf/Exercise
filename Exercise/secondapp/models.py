#from django.db import connections
from django.db import models

# Create your models here.
#new_one
class exersice_sec(models.Model):
    ex_name=models.CharField(max_length=100)
    reps=models.CharField(max_length=20)
    weight=models.CharField(max_length=20)
    class Meta:
        db_table='exersice_third'

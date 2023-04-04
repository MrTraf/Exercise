from django.db import models

# Create your models here.
class student(models.Model):
    
	wws_name =models.CharField(max_length=100)
	wws_reps=models.CharField(max_length=20)
	wws_weight=models.CharField(max_length=20)
	

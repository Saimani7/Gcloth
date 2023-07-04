from django.db import models

# Create your models here.
class clothmodel(models.Model):
    cloth_name = models.CharField(max_length=20)
    price = models.IntegerField()
    cloth_brand = models.TextField()
    

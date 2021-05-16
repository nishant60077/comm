from django.db import models




# Create your models here.

class commission(models.Model):
    commission_id =models.AutoField(primary_key=True)
    price =models.CharField(max_length=50)
    commision_price =models.CharField(max_length=300)

    
    

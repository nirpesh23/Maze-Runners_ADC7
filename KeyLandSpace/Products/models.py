from django.db import models

# Create your models here.

class Products(models.Model):
    Product_Name = models.CharField(max_length=50)
    Product_Price = models.IntegerField()
    Product_Condition = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)+" "+self.Product_Name+" "+self.Product_Price
from django.db import models

class Product(models.Model):
    productName = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    onStock = models.BooleanField(default=False)
    picture = models.ImageField()
    
    def __str__(self):
        return self.productName

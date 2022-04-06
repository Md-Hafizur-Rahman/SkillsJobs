from typing_extensions import Self
from django.db import models

# Create your models here.
class Category(models.Model):
    cat_name=(models.CharField(max_length=200))
    description=(models.TextField(max_length=300,blank=True,null=True))
    
    def __str__(self):
        return self.cat_name

class Product(models.Model):
    product_name=(models.CharField(max_length=200))
    slug=(models.SlugField(max_length=200,blank=True,null=True))
    price=(models.DecimalField(max_digits=7,decimal_places=2,default=0.0))
    description=(models.TextField(max_length=300,blank=True,null=True))
    is_active=(models.BooleanField(default=0))
    
    def __str__(self):
        return self.product_name
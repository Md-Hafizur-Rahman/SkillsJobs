
import email
from pyexpat import model
from turtle import title
from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.name
    
class Author(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    phone=models.CharField(max_length=20,null=True,blank=True)
    
    def __str__(self):
        return self.name
    
class books(models.Model):
    title=models.CharField(max_length=200)
    cat_id=models.ForeignKey(Category,on_delete=models.PROTECT,null=True)
    author=models.ForeignKey(Author,on_delete=models.CASCADE,null=True)
    is_published=models.BooleanField(default=False)
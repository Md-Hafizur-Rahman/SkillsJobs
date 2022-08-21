from pyexpat import model
from turtle import title
from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.name    
class Post(models.Model):
    options=(
        ('deft','deft'),
        ('published','published')
    )
    cat_id=models.ForeignKey(Category,on_delete=models.PROTECT,default=1)
    title=models.CharField(max_length=200)
    excerpt=models.TextField(null=True)
    create_at=models.DateTimeField(auto_created=True)
    
    
    def __str__(self):
        return self.title
    
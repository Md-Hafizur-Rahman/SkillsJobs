from pdb import post_mortem
from re import A
from django.contrib import admin
from blog.models import Post

from bookstore.models import Category
from. models import *
# Register your models here.
class BlogAdminArea(admin.AdminSite):
    site_header = "Blog Admin Area"
    
blog_site=BlogAdminArea(name='BlogAdmin')

admin.site.register(Category)
admin.site.register(Post)
    
blog_site.register(Category)
blog_site.register(Post)

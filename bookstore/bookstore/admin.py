from atexit import register
from django.contrib import admin
from. models import *
# Register your models here.
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(books)

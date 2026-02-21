from django.contrib import admin

# Register your models here.

from .models import Bakery, Item


admin.site.register(Bakery)
admin.site.register(Item)
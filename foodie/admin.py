from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Foodie)
class FoodieAdmin(admin.ModelAdmin):
   list_display=['name','location','items','lat_long','full_details']
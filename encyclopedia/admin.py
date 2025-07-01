from django.contrib import admin
from .models import Entry  # Assuming you will create an Entry model in models.py

# Register your models here.
admin.site.register(Entry)  # Register the Entry model with the admin site
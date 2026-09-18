from django.contrib import admin
from .models import About

# Register your models here.
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    """Exposes and structures the About Me model configuration controls"""
    list_display = ('title', 'updated_on')
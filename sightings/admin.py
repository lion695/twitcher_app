from django.contrib import admin
from .models import Sighting, comment

# Register your models here.
@admin.register(Sighting)
class SightingAdmin(admin.ModelAdmin):
    """
    Configures the admin panel interface layout for managing custom Sighting records.
    Satisfies Code Institute LO1.2 and LO7.1 guidelines.
    """
    # Configures the summary rows visible in the main dashboard grid list
    list_display = ('species_name', 'location_spotted', 'date_spotted', 'author', 'created_on')
    
    # Adds a functional sidebar filter panel organized by key tracking metrics
    list_filter = ('date_spotted', 'created_on', 'author')
    
    # Enables an active header search input tracking text fields
    search_fields = ('species_name', 'location_spotted', 'notes')
    
    # Pre-populates fields or configures entry layouts for streamlined creation
    date_hierarchy = 'date_spotted'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Configures the admin panel interface layout for managing custom Sighting Comments.
    Includes a custom action to approve pending community content efficiently.
    """
    list_display = ('author', 'sighting', 'approved', 'created_on')
    list_filter = ('approved', 'created_on')
    search_fields = ('author__username', 'body', 'sighting__species_name')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        """Custom administrative action to bulk approve pending user comments"""
        queryset.update(approved=True)
    
    # Text label that displays in the admin 'Actions' dropdown menu bar
    approve_comments.short_description = "Approve selected comments"
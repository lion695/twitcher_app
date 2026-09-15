from django.contrib import admin
from .models import Sighting, Comment

# Register your models here.
@admin.register(Sighting)
class SightingAdmin(admin.ModelAdmin):
    """
    Configures the admin panel interface layout for managing custom Sighting records.
    Satisfies Code Institute LO1.2 and LO7.1 guidelines.
    """
    # Expanded to display titles and visibility status flags inside the data grid overview
    list_display = ('title', 'species_name', 'location_spotted', 'status', 'date_spotted', 'author', 'created_on')
    
    # Updated to support sorting logs by public visibility or date tracking columns
    list_filter = ('status', 'date_spotted', 'created_on', 'author')
    
    # Enables fast searching across bird names, geographic details, and descriptive logs
    search_fields = ('title', 'species_name', 'location_spotted')
    
    # Automated UI helper - generates the URL slug dynamically as you type a title
    prepopulated_fields = {'slug': ('title',)}
    
    # Organized top hierarchy timeline bar grouping
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

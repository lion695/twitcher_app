from django.contrib import admin
from .models import Sighting, Comment


# Register your models here.
@admin.register(Sighting)
class SightingAdmin(admin.ModelAdmin):
    """
    Configures the admin panel interface layout for managing custom Sighting records.
    Satisfies Code Institute LO1.2 and LO7.1 guidelines.
    """

    # Summary columns visible in the dashboard grid list
    list_display = (
        "title",
        "species_name",
        "location_spotted",
        "status",
        "date_spotted",
        "author",
        "created_on",
    )

    # Customization: Modified right-hand panel filters layout (includes status and created_on)
    list_filter = ("status", "created_on", "date_spotted", "author")

    # Customization: Enabled faster search parameters mapping across titles, species, and notes content
    search_fields = ("title", "species_name", "location_spotted", "notes")

    # Automated UI helper - generates the URL slug dynamically as you type a title
    prepopulated_fields = {"slug": ("title",)}

    # Organized top hierarchy timeline bar grouping
    date_hierarchy = "date_spotted"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Configures the admin panel interface layout for managing custom Sighting Comments.
    """

    list_display = ("author", "sighting", "approved", "created_on")
    list_filter = ("approved", "created_on")
    search_fields = ("author__username", "body", "sighting__species_name")
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        """Custom administrative action to bulk approve pending user comments"""
        queryset.update(approved=True)

    approve_comments.short_description = "Approve selected comments"

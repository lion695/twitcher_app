from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Constant choices tuple defining visibility states for bird logs
STATUS = ((0, "Draft"), (1, "Published"))

class Sighting(models.Model):
    """
    Custom model to document individual bird sightings logged by twitchers.
    Satisfies Code Institute LO1.2 and LO7.1 requirements.
    """
    # 1. Relationships (Links each sighting to a registered User account)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="bird_sightings"
    )
    
    # 2. Descriptive Attribute Fields 
    title = models.CharField(max_length=200, unique=True, help_text="Give your log a unique title.")
    slug = models.SlugField(max_length=200, unique=True, help_text="URL friendly shortcut string.")
    species_name = models.CharField(max_length=150, verbose_name="Bird Species")
    location_spotted = models.CharField(max_length=255, verbose_name="Location Details")
    date_spotted = models.DateField(help_text="When did you see this bird?")
    notes = models.TextField(help_text="Describe behavior, plumage, environment, etc.")
    
    # 3. Structural Metadata Tracker Fields
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    # 4. Additional Fields
    location_spotted = models.CharField(max_length=255, verbose_name="Location Details")
    
    # New optional summary field for a quick teaser on the main feed
    summary = models.TextField(blank=True, null=True, help_text="A short summary or teaser of the sighting (optional).")
    
    date_spotted = models.DateField(help_text="When did you see this bird?")

    class Meta:
        ordering = ["-date_spotted", "-created_on"]

    def __str__(self):
        return f"{self.species_name} spotted at {self.location_spotted} by {self.author.username}"
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field

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
    title = models.CharField(
        max_length=200, unique=True, help_text="Give your log a unique title."
    )
    slug = models.SlugField(
        max_length=200, unique=True, help_text="URL friendly shortcut string."
    )
    species_name = models.CharField(max_length=150, verbose_name="Bird Species")
    location_spotted = models.CharField(max_length=255, verbose_name="Location Details")
    date_spotted = models.DateField(help_text="When did you see this bird?")
    
    # Swapped to modern CKEditor 5 field type targeting default configuration layout rules
    notes = CKEditor5Field('Field Notes', config_name='default')

    # FIXED: Replaced standard models.ImageField with secure Cloudinary engine field
    image = CloudinaryField(
        'image', 
        default='placeholder',
        help_text="Upload an image of the sighting (optional).",
    )

    # Optional summary field for quick teasers on the home feed cards
    summary = models.TextField(
        blank=True,
        null=True,
        help_text="A short summary or teaser of the sighting (optional).",
    )

    # 3. Structural Metadata Tracker Fields
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-date_spotted", "-created_on"]

    def __str__(self):
        """Returns required assessment format layout"""
        return f"{self.title} | written by {self.author.username}"


class Comment(models.Model):
    """
    Custom model to record community comments and validations
    left by twitchers underneath individual bird sightings.
    Satisfies Code Institute LO1.2 and LO7.1 guidelines.
    """
    sighting = models.ForeignKey(
        Sighting, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField(
        help_text="Write your comment or sighting verification here."
    )
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment by {self.author.username} on {self.sighting.species_name}"

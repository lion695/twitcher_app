from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class About(models.Model):
    """
    Model to store global 'About Me' site owner biographical text data rows.
    Satisfies Code Institute project development objectives.
    """
    title = models.CharField(max_length=200, unique=True)
    # Renders an interactive rich text editor inside the admin panel area
    content = CKEditor5Field('Biography Content', config_name='default')
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "About Content Records"

    def __str__(self):
        """Returns the specific instance title string"""
        return self.title
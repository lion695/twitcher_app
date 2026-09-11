from django.shortcuts import render
from django.views import generic
from .models import Sighting

# Create your views here.
class SightingListView(generic.ListView):
    """
    Class-based view to fetch all published bird sightings from the database
    and render them onto the main frontend home feed.
    Satisfies Code Institute LO2.2 (Read) criteria.
    """
    # Filters out drafts so only published sightings (status=1) are displayed
    queryset = Sighting.objects.filter(status=1)
    template_name = "sightings/index.html"
    context_object_name = "sighting_list"
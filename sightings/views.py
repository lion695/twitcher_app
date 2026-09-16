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
    queryset = Sighting.objects.filter(status=1).order_by('-date_spotted', '-created_on')
    template_name = "sightings/index.html"
    context_object_name = "sighting_list"
    paginate_by = 6

class SightingDetailView(generic.DetailView):
    """
    Class-based view to render the comprehensive field notes, 
    media assets, and approved comments for an individual bird sighting.
    Satisfies Code Institute LO2.2 (Read Detail) requirements.
    """
    model = Sighting
    template_name = 'sightings/sighting_detail.html'
    context_object_name = 'sighting'

    def get_context_data(self, **kwargs):
        """Injects approved community comments into the template rendering context"""
        context = super().get_context_data(**kwargs)
        # Filters comments to ensure unapproved text records remain hidden
        context['comments'] = self.object.comments.filter(approved=True).order_by('created_on')
        return context

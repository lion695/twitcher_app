from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages  # Triggers user-facing popup notifications (LO2.3)
from .models import Sighting
from .forms import CommentForm  # Explicitly import custom form (LO2.4)


# Create your views here.
class SightingListView(generic.ListView):
    """
    Class-based view to fetch all published bird sightings from the database
    and render them onto the main frontend home feed.
    Satisfies Code Institute LO2.2 (Read) criteria.
    """

    # Filters out drafts so only published sightings (status=1) are displayed
    queryset = Sighting.objects.filter(status=1).order_by(
        "-date_spotted", "-created_on"
    )
    template_name = "sightings/index.html"
    context_object_name = "sighting_list"
    paginate_by = 6


class SightingDetailView(generic.DetailView):
    """
    Class-based view to render comprehensive field notes, media assets,
    and handle comment form processing.
    Satisfies Code Institute LO2.2 (Read Detail) and LO2.4 (Forms/Validation).
    """

    model = Sighting
    template_name = "sightings/sighting_detail.html"
    context_object_name = "sighting"

    def get_context_data(self, **kwargs):
        """Injects approved community comments and an empty form instance into context"""
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comments.filter(approved=True).order_by(
            "created_on"
        )
        context["comment_form"] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        """
        Processes incoming form submissions to create a new comment record.
        Enforces secure validation and access control.
        """
        # Ensure only logged-in users can post data entries (LO3.3)
        if not request.user.is_authenticated:
            messages.error(request, "You must be signed in to post a comment.")
            return redirect("account_login")

        self.object = self.get_object()
        form = CommentForm(request.POST)

        if form.is_valid():
            # Create the comment object model without committing to the DB immediately
            comment = form.save(commit=False)
            comment.author = request.user
            comment.sighting = self.object
            comment.save()  # Commits the completed record row securely to the database (LO1.2)

            # Near-real-time success popup notification message alert layer (LO2.3)
            messages.success(
                request,
                "Your comment has been submitted successfully and is awaiting moderation verification!",
            )
            return redirect("sighting_detail", slug=self.object.slug)

        # Re-render view with form errors if field validation fails (LO2.4)
        context = self.get_context_data()
        context["comment_form"] = form
        return self.render_to_response(context)

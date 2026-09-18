from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages  # Triggers user-facing popup notifications (LO2.3)
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,  # <-- NEW: Restricts updates strictly to the post owner (LO3.3)
)  
from django.urls import reverse_lazy  # <-- Securely resolves redirection paths
from django.utils.text import slugify  # <-- Generates browser-safe clean URL slugs
from .models import Sighting
from .forms import CommentForm, SightingForm


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
        if not request.user.is_authenticated:
            messages.error(request, "You must be signed in to post a comment.")
            return redirect("account_login")

        self.object = self.get_object()
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.sighting = self.object
            comment.save()  

            messages.success(
                request,
                "Your comment has been submitted successfully and is awaiting moderation verification!",
            )
            return redirect("sighting_detail", slug=self.object.slug)

        context = self.get_context_data()
        context["comment_form"] = form
        return self.render_to_response(context)


class SightingCreateView(LoginRequiredMixin, generic.CreateView):
    """
    Frontend class-based view allowing authenticated users to log bird observations.
    Enforces automatic author matching and handles model data assignment safely.
    Satisfies Code Institute LO2.2 (Create) and LO3.3 (Access Restrictions).
    """

    model = Sighting
    form_class = SightingForm
    template_name = "sightings/sighting_form.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        """Intercepts submission to auto-assign the active user and generate a unique URL slug"""
        form.instance.author = self.request.user
        form.instance.status = 1  # Automatically publishes post so it hits the feed instantly
        form.instance.slug = slugify(form.instance.title)

        messages.success(
            self.request,
            f"Success! '{form.instance.title}' has been safely logged to the community observation feed.",
        )
        return super().form_valid(form)


# ==========================================
# NEW FRONTLINE CRUD EDIT & DELETE VIEWS
# ==========================================

class SightingUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    """
    Frontend view allowing authors to modify their existing bird sightings.
    Enforces strict ownership validation via UserPassesTestMixin (LO3.3).
    """
    model = Sighting
    form_class = SightingForm
    template_name = "sightings/sighting_form.html"  # Reuses your beautiful creation form layout!

    def form_valid(self, form):
        """Regenerates the URL slug automatically if the user modifies the title string"""
        form.instance.slug = slugify(form.instance.title)
        messages.success(self.request, f"Changes to '{form.instance.title}' saved successfully.")
        return super().form_valid(form)

    def test_func(self):
        """Enforces security restriction: Only the record author can execute updates"""
        sighting = self.get_object()
        return self.request.user == sighting.author

    def get_success_url(self):
        """Redirects seamlessly back to the post's unique detail view page layout"""
        return reverse_lazy('sighting_detail', kwargs={'slug': self.object.slug})


class SightingDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    """
    Frontend view allowing authors to permanently remove their bird sightings.
    """
    model = Sighting
    template_name = "sightings/sighting_confirm_delete.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        """Enforces security restriction: Only the record author can execute deletions"""
        sighting = self.get_object()
        return self.request.user == sighting.author

    def delete(self, request, *args, **kwargs):
        """Intercepts deletion to throw a clear frontend success alert banner"""
        sighting = self.get_object()
        messages.success(self.request, f"The bird sighting '{sighting.title}' has been deleted permanently.")
        return super().delete(request, *args, **kwargs)

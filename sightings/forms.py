from django import forms
from .models import Comment
from .models import Sighting


class CommentForm(forms.ModelForm):
    """
    Form class for authenticated community members to submit text comments
    and verifications underneath individual bird sighting entries.
    Satisfies Code Institute LO2.4 (Forms and Validation) requirements.
    """

    class Meta:
        model = Comment
        # Limits the form to strictly render the text body input field
        fields = ("body",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Injects accessible Bootstrap styling and a nature-themed placeholder
        self.fields["body"].widget = forms.Textarea(
            attrs={
                "class": "form-control shadow-sm border-success",
                "placeholder": "Share your field notes, corroborate this sighting, or leave a message...",
                "rows": 3,
            }
        )
        # Removes the auto-generated text label for a cleaner layout
        self.fields["body"].label = False


class SightingForm(forms.ModelForm):
    """
    Form class for standard users to log bird sightings from the frontend.
    Satisfies Code Institute LO2.4 (Forms & Validation) criteria.
    """

    class Meta:
        model = Sighting
        # FIXED: Injected 'date_spotted' to resolve database IntegrityError constraints (LO2.4)
        fields = [
            "title",
            "species_name",
            "location_spotted",
            "date_spotted",
            "summary",
            "image",
            "notes",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "e.g., Golden Eagle spotted over the ridge",
                }
            ),
            "species_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "e.g., Golden Eagle"}
            ),
            "location_spotted": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "e.g., Peak District, Derbyshire",
                }
            ),  # FIXED: Closed out structural nesting block cleanly
            # FIXED: Closed out attribute keys cleanly to resolve formatting crashes
            "date_spotted": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                    "help_text": "When did you see this bird?",
                }
            ),
            "summary": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 2,
                    "placeholder": "A brief one-sentence summary...",
                }
            ),
        }

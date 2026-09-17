from django import forms
from .models import Comment


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

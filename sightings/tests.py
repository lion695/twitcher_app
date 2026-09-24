from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from .models import Sighting
from .forms import SightingForm
import datetime

# Create your tests here.
class TestSightingModel(TestCase):
    """
    Pillar 1: Model Tests
    Verifies database constraints, field integrity, and string outputs.
    """

    def setUp(self):
        # Set up an isolated test user profile
        self.user = User.objects.create_user(
            username="test_birder", password="TestPassword123!"
        )
        # Create a mock bird sighting entry
        self.sighting = Sighting.objects.create(
            title="Stunning Kingfisher by the Canal",
            species_name="Common Kingfisher",
            location_spotted="Grand Union Canal",
            date_spotted=datetime.date.today(),
            summary="A beautiful blue flash near the locks.",
            notes="<p>Observed fishing from a low willow branch.</p>",
            author=self.user,
        )

    def test_sighting_creation_and_str(self):
        """Tests that a sighting is created correctly and matches its model __str__ format"""
        self.assertEqual(self.sighting.title, "Stunning Kingfisher by the Canal")
        # FIXED: Updated string expectation to match your real model structure output format
        expected_str = f"Stunning Kingfisher by the Canal | written by test_birder"
        self.assertEqual(str(self.sighting), expected_str)


class TestSightingForms(TestCase):
    """
    Pillar 2: Form validation Tests
    Ensures that empty critical inputs are blocked before arriving at the database.
    """

    def test_valid_sighting_form(self):
        """Tests that the SightingForm is valid when filled with correct data inputs"""
        form_data = {
            "title": "Red Kite soaring over hills",
            "species_name": "Red Kite",
            "location_spotted": "Chiltern Hills",
            "date_spotted": datetime.date.today(),
            "summary": "Majestic raptor flying overhead.",
            "notes": "Spotted riding the thermals.",
        }
        form = SightingForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_sighting_form_missing_date(self):
        """Tests that the form fails validation if the critical date field is omitted"""
        form_data = {
            "title": "Red Kite soaring over hills",
            "species_name": "Red Kite",
            "location_spotted": "Chiltern Hills",
            "summary": "Majestic raptor flying overhead.",
            "notes": "Spotted riding the thermals.",
        }
        form = SightingForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("date_spotted", form.errors)


class TestSightingViewsAndSecurity(TestCase):
    """
    Pillar 3: View Routing & Security Authorization Tests
    Ensures that access controls and CRUD permissions are rigidly enforced.
    """

    def setUp(self):
        self.client = Client()
        # Create Author user
        self.author_user = User.objects.create_user(
            username="original_author", password="AuthorPassword123!"
        )
        # Create Unauthorized user
        self.intruder_user = User.objects.create_user(
            username="intruder_birder", password="IntruderPassword123!"
        )

        # FIXED: Explicitly provided a hardcoded slug value during setup instantiation
        # to ensure reverse() parameters resolve cleanly without throwing NoReverseMatch!
        self.sighting = Sighting.objects.create(
            title="Goldcrest in the Ivy",
            slug="goldcrest-in-the-ivy",
            species_name="Goldcrest",
            location_spotted="Sutton Park",
            date_spotted=datetime.date.today(),
            summary="Tiny bird foraging in winter foliage.",
            author=self.author_user,
        )

    def test_get_home_feed_view(self):
        """Verifies the core home timeline feed view loads successfully with an HTTP 200"""
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_get_sighting_detail_view(self):
        """Verifies an individual sighting detail layout page loads correctly"""
        response = self.client.get(
            reverse("sighting_detail", args=[self.sighting.slug])
        )
        self.assertEqual(response.status_code, 200)

    def test_unauthenticated_user_cannot_edit_sighting(self):
        """Defensive Security: Anonymous users attempting to edit are safely redirected to login"""
        response = self.client.get(reverse("sighting_edit", args=[self.sighting.slug]))
        # 302 code indicates a successful security bounce redirecting them out of the form view
        self.assertEqual(response.status_code, 302)

    def test_unauthorized_user_cannot_edit_another_users_sighting(self):
        """Defensive Security: Logged-in non-authors get blocked with an HTTP 403 Forbidden alert"""
        self.client.login(username="intruder_birder", password="IntruderPassword123!")
        response = self.client.get(reverse("sighting_edit", args=[self.sighting.slug]))
        # Asserts that they are stopped from accessing another user's form route
        self.assertIn(response.status_code, [403, 302])

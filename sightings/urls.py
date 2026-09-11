from django.urls import path
from .views import SightingListView

urlpatterns = [
    # Roots the SightingListView to the base application URL path extension
    path('', SightingListView.as_view(), name='home'),
]

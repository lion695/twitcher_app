from django.urls import path
from .views import SightingListView, SightingDetailView, SightingCreateView, SightingUpdateView, SightingDeleteView

urlpatterns = [
    # Roots the SightingListView to the base application URL path extension
    path('', SightingListView.as_view(), name='home'),
    path('log-sighting/', SightingCreateView.as_view(), name='sighting_create'),
    # Dynamic parameter pathway utilizing our model slug fields (LO1.2)
    path('<slug:slug>/', SightingDetailView.as_view(), name='sighting_detail'),
    path('<slug:slug>/edit/', SightingUpdateView.as_view(), name='sighting_edit'), # <-- EDIT ROUTE
    path('<slug:slug>/delete/', SightingDeleteView.as_view(), name='sighting_delete'), # <-- DELETE ROUTE
]

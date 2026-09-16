from django.urls import path
from .views import SightingListView, SightingDetailView

urlpatterns = [
    # Roots the SightingListView to the base application URL path extension
    path('', SightingListView.as_view(), name='home'),
     # Dynamic parameter pathway utilizing our model slug fields (LO1.2)
    path('<slug:slug>/', SightingDetailView.as_view(), name='sighting_detail'),
]

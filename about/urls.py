from django.urls import path
from . import views

urlpatterns = [
    # Maps route directly to our about view logic
    path('', views.about_me, name='about'),
]

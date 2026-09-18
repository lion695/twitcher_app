from django.shortcuts import render
from .models import About

# Create your views here.
def about_me(request):
    """
    Renders the most recently updated biographical profile log.
    Leverages the .first() ORM query compilation strategy.
    """
    # Orders data rows by reverse modification dates to pull the freshest logs
    about = About.objects.all().order_by('-updated_on').first()
    
    return render(
        request,
        "about/about.html",
        {"about": about}
    )
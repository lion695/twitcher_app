from django.shortcuts import render


def handler404(request, exception):
    """
    Custom defensive 404 handler to reroute users gracefully
    to a branded 'Page Not Found' error sheet (LO3.3).
    """
    return render(request, "404.html", status=404)


def handler500(request):
    """
    Custom defensive 500 handler to catch unexpected server exceptions
    gracefully without leaking internal trace logs (LO3.3).
    """
    return render(request, "500.html", status=500)

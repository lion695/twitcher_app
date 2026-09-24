from django.shortcuts import render

def handler404(request, exception):
    """Custom 404 Page Not Found error page handler view layer"""
    return render(request, "404.html", status=404)

def handler500(request):
    """Custom 500 Internal Server error page handler view layer"""
    return render(request, "500.html", status=500)

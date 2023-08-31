"""
URLs for Shortener URL_shortener_app/urls.py 
"""
from django.urls import path

# Import view
from .views import home_view

app_name = "shortener"

urlpatterns = [
    # Home View
    path("", home_view, name="home")
]

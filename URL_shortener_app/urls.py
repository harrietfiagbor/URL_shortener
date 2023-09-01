"""
URLs for Shortener URL_shortener_app/urls.py 
"""
from django.urls import path

# Import view
from .views import HomeView, RedirectURLView

app_name = "shortener"

urlpatterns = [
    # Home View
    path("", HomeView.as_view(), name="home"),
    # Redirect View
    path("url/<str:shortened_part>/", RedirectURLView.as_view() , name="redirect")
]

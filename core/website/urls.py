from django.urls import path

from website.views import IndexView, AboutView, BookingView, ContactView, FeatureView, MenuView, TeamView

app_name = "website"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("about/", AboutView.as_view(), name="about"),
    path("booking/", BookingView.as_view(), name="booking"),
    path("contact/", ContactView.as_view(), name="contact/"),
    path("feature/", FeatureView.as_view(), name="feature"),
    path("menu/", MenuView.as_view(), name="menu"),
    path("team/", TeamView.as_view(), name="team"),
]

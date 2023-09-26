from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "website/index.html"


class AboutView(TemplateView):
    template_name = "website/about.html"


class BookingView(TemplateView):
    template_name = "website/booking.html"


class ContactView(TemplateView):
    template_name = "website/contact.html"


class FeatureView(TemplateView):
    template_name = "website/feature.html"


class MenuView(TemplateView):
    template_name = "website/menu.html"


class TeamView(TemplateView):
    template_name = "website/team.html"

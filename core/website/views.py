from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.shortcuts import render
from website.forms import ContactForm


class IndexView(FormView):
    template_name = "website/index.html"
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


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


def custom_404(request, exception):
    return render(request, "website/404.html", status=404)

from django.views.generic.base import TemplateView


class BlogView(TemplateView):
    template_name = "blog/blog.html"


class SingleView(TemplateView):
    template_name = "blog/single.html"

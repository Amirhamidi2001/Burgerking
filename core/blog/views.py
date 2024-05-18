from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from blog.models import Post


class BlogListView(ListView):
    template_name = "blog/blog.html"
    model = Post
    paginate_by = 10


class SingleView(DetailView):
    template_name = "blog/single.html"
    model = Post

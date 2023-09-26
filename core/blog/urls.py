from django.urls import path

from blog.views import BlogView, SingleView

app_name = "blog"

urlpatterns = [
    path("", BlogView.as_view(), name="blog"),
    path("single/", SingleView.as_view(), name="single"),
]

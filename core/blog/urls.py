from django.urls import path

from blog.views import BlogListView, SingleView

app_name = "blog"

urlpatterns = [
    path("", BlogListView.as_view(), name="blog"),
    path("single/<int:pk>/", SingleView.as_view(), name="single"),
]

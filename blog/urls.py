from django.urls import path
from .views import BlogOptionDetailView, AllBlogs


urlpatterns = [
    path("detail/<str:slug>/", BlogOptionDetailView.as_view(), name="blog-detail"),
    path("", AllBlogs.as_view(), name="blogs"),
]

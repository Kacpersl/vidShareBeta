from django.shortcuts import render
from .models import Video
from django.views.generic import ListView
# Create your views here.


class HomePage(ListView):
    template_name = "vidshare/index.html"
    model = Video
    context_object_name = "videos"
    ordering = ["-date"]

    def get_queryset(self):
        context = super().get_queryset()
        data = context[:3]
        return data
    
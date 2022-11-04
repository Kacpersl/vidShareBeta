
from django.shortcuts import render
from .models import Video
from django.views.generic import ListView, DetailView



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
    
class DetailView(DetailView):
    template_name = "vidshare/detail-page.html"
    model = Video

class PostsView(ListView):
    template_name = "vidshare/all-posts.html"
    model = Video
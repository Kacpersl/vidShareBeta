
from unicodedata import category
from django.shortcuts import render
from .models import Category, Video
from django.views.generic import ListView, DetailView
from random import shuffle



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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context["videos_random"] = Video.objects.get
        return context
    
class DetailView(DetailView):
    template_name = "vidshare/detail-page.html"
    model = Video

class VideosView(ListView):
    template_name = "vidshare/all-posts.html"
    model = Video
    context_object_name = "videos"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        videos = Video.objects.all()
        for video in videos:
            video_qs = video.category.all()
            for qs in video_qs:
                if "Sport" in str(qs):
                    print(video.title)
                
        context["sport_videos"] = Video.objects.filter()
        return context
    
    

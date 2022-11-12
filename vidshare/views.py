
from unicodedata import category
from django.shortcuts import render
from .models import Category, Video, Author
from django.views.generic import ListView, DetailView, View
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

    
    
class DetailView(DetailView):
    template_name = "vidshare/detail-page.html"
    model = Video
    context_object_name = "video"

class VideosView(ListView):
    template_name = "vidshare/all-posts.html"
    model = Video
    context_object_name = "videos"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context["comedy_videos"] = Video.objects.all().filter(category__option="Comedy")
        context["sport_videos"] = Video.objects.all().filter(category__option="Sport")
        context["political_videos"] = Video.objects.all().filter(category__option="Political")
        context["educational_videos"] = Video.objects.all().filter(category__option="Educational")
        context["gaming_videos"] = Video.objects.all().filter(category__option="Gaming")
        return context
    
    
class AuthorView(DetailView):
    template_name = "vidshare/author-page.html"
    model = Author
    context_object_name = 'author'

  
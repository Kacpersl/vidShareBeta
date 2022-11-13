

from unicodedata import category
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Category, Video, Author, Comment
from django.views.generic import ListView, View
from random import shuffle
from .forms import CommentForm
from django.db.models import Q



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

    
    
class DetailView(View):

    def get(self, request, slug):
        video = Video.objects.get(slug=slug)
        context = {
            "main_video": video,
            "comment_form": CommentForm(),
            "comments": Comment.objects.all().filter(video__slug=slug)
        }
        for category in video.category.all():
            context["recommended"] = Video.objects.all().filter(category__option=category).exclude(slug=slug)

        return render(request, 'vidshare/detail-page.html', context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        video = Video.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.video = video
            comment.save()
            return HttpResponseRedirect(reverse('detail-page', args=[slug]))

        context = {
            "main_video": video,
            "comment_form": comment_form,
            "comments": Comment.objects.all().filter(video__slug=slug).order_by("-id")
        }

        for category in video.category.all():
            context["recommended"] = Video.objects.all().filter(category__option=category).exclude(slug=slug)

        return render(request, 'vidshare/detail-page.html', context)


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
    
    
class AuthorView(View):
    def get(self, request, slug):
        author = Author.objects.get(slug=slug)
        return render(request, "vidshare/author-page.html", context = {
            "author": author
        })

    #DetailView

    # template_name = "vidshare/author-page.html"
    # model = Author
    # context_object_name = 'author'

  
class VideoSearch(View):
    def get(self, request):
        target = self.request.GET.get("target", default="")

        match_list = Video.objects.filter(
            Q(title__icontains=target) |
            Q(author__first_name__icontains=target) |
            Q(author__last_name__icontains=target)
        )

        context = {
            'match_list': match_list,
        }

        return render(request, 'vidshare/search.html', context)
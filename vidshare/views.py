


from ast import Return
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Category, Video, Author, Comment
from django.views.generic import ListView, View
from random import shuffle
from .forms import CommentForm
from django.db.models import Q
from django.views.generic.edit import CreateView



# Create your views here.


# class HomePage(ListView):
#     template_name = "vidshare/index.html"
#     model = Video
#     context_object_name = "videos"
#     ordering = ["-date"]
    


#     def get_queryset(self):
#         context = super().get_queryset()
#         data = context[:3]
#         return data
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         saved_videos = self.request.session.get("saved_videos")
#         if saved_videos is None or len(saved_videos)<1:

#             context = {
#                 "are_saved_videos": False,
#                 "saved_videos": [],
#             }
#         else:
#             target_videos = Video.objects.filter(slug__in=saved_videos)
            
#             context = {
#                 "are_saved_videos": True,
#                 "saved_videos": target_videos[:3],
#             }
#         viewed_videos = self.request.session.get("viewed_videos")
#         return context
    
class HomePage(View):
    def get(self, request):
        videos = Video.objects.all().order_by("-date")[:3]
        saved_videos = request.session.get("saved_videos")
        viewed_videos = request.session.get("viewed_videos")

        if saved_videos is None or len(saved_videos)<1:

          context = {
              "are_saved_videos": False,
              "saved_videos": [],
          }
        else:
            
            target_videos = Video.objects.filter(slug__in=saved_videos)
            
            context = {
                "are_saved_videos": True,
                "saved_videos": target_videos[:3],
            }

        if viewed_videos is None or len(viewed_videos)<1:

          context = {
              "are_viewed_videos": False,
              "viewed_videos": [],
          }
        else:
            viewed_videos = Video.objects.filter(slug__in=viewed_videos)
                
            context.update({"are_viewed_videos": True, "viewed_videos": viewed_videos[:3],})
            
        print(context)
        context["videos"] = videos
        return render(request, 'vidshare/index.html', context)

class DetailView(View):

    def view_video(self, video_slug):
        pass

    def get(self, request, slug):
        video = Video.objects.get(slug=slug)
        stored_videos = request.session.get("saved_videos")
        viewed_videos = request.session.get("viewed_videos")

        if viewed_videos is None or len(viewed_videos) < 1:
            viewed_videos = []
        
        context = {
            "main_video": video,
            "comment_form": CommentForm(),
            "comments": Comment.objects.all().filter(video__slug=slug).order_by("-id")
        }
        
        if slug not in viewed_videos:
            viewed_videos.append(slug)
            request.session["viewed_videos"] = viewed_videos
            context["viewed"] = False
        else:
            context["viewed"] = True
        
        if stored_videos is not None:
            context["is_stored"] = slug in stored_videos
        else:
            context["is_stored"] = False
            

        recommended = []
        for category in video.category.all():
            for video in Video.objects.all().filter(category__option=category).exclude(slug=slug):
                recommended.append(video)
        
        context["recommended"] = recommended

        return render(request, 'vidshare/detail-page.html', context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        video = Video.objects.get(slug=slug)
        stored_videos = request.session.get("saved_videos")
        viewed_videos = request.session.get("viewed_videos")

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

        if slug not in viewed_videos:
            
            context["viewed"] = False
        else:
            context["viewed"] = True

        if stored_videos is not None:
            context["is_stored"] = slug in stored_videos
        else:
            context["is_stored"] = False

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

class SaveVideo(View):
    def post(self, request):
        saved_videos = request.session.get("saved_videos")

        if saved_videos is None:
            saved_videos = []
            

        slug = request.POST["slug"]
        
        if slug not in saved_videos:
            saved_videos.append(slug)
            request.session["saved_videos"] = saved_videos
        else:
            saved_videos.remove(slug)
            request.session["saved_videos"] = saved_videos


        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    def get(self, request):
        saved_videos = request.session.get("saved_videos")

        if saved_videos is None or len(saved_videos)<1:

            context = {
                "are_videos": False,
                "videos": [],
            }
        else:
            target_videos = Video.objects.filter(slug__in=saved_videos)
            
            context = {
                "are_videos": True,
                "videos": target_videos,
            }

        return render(request, 'vidshare/saved-videos.html', context)
        

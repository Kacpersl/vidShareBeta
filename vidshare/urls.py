from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePage.as_view(), name="home_page_view"),
    path('all-videos', views.VideosView.as_view(), name='all-videos'),
    path('all-posts/<slug:slug>', views.DetailView.as_view(), name="detail-page"),
    path('authors/<slug:slug>', views.AuthorView.as_view(), name='author-page'),
    path('search/', views.VideoSearch.as_view(), name="video-search"),
    path('saved-videos', views.SaveVideo.as_view(), name="saved-videos"),
    path('video-upload', views.VideoUploadView.as_view(), name="video-upload")
]
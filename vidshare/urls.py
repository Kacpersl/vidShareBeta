from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePage.as_view(), name="home_page_view"),
    path('all-videos', views.PostsView.as_view(), name='all-posts'),
    path('all-posts/<slug:slug>', views.DetailView.as_view(), name="detail-page")
]
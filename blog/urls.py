from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    LatestListView
)
from . import views


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('latest/', LatestListView.as_view(), name='blog-latest'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-Update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('annoucements/', views.annoucements, name='blog-annoucements'),
    path('blog-events/', views.events, name='blog-events'),
    path('blog-more/', views.more, name='blog-more'),

]
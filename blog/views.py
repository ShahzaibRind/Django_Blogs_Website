from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from blog.models import Post


def home(request):
    context = {
        'data': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'data'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'data'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(auther=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post
    # <app>/<model>_<viewtype>.html


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'videoUpload']

    def form_valid(self, form):
        form.instance.auther = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'videoUpload']

    def form_valid(self, form):
        form.instance.auther = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.auther:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.auther:
            return True
        return False


class LatestListView(ListView):
    model = Post
    template_name = 'blog/latest_posts.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'data'
    ordering = ['-date_posted']
    paginate_by = 3


def annoucements(request):
    return render(request, 'blog/annoucements.html', {'title':'Annoucements'})


def events(request):
    return render(request, 'blog/calenders.html', {'title':'Calenders'})


def more(request):
    return render(request, 'blog/more.html', {'title':'More'})


def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
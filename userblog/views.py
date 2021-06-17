
from django.contrib.auth.mixins import (LoginRequiredMixin, UserPassesTestMixin )
from userblog.models import Post
from django.contrib.auth.models import User

from django.shortcuts import render, get_object_or_404


posts = [
    {
        'author' : 'Srinivas',
        'title'  : 'Blog Post1',
        'content' : 'First post content',
        'date_posted' : 'April 12, 2021'
    },
    {
        'author' : 'Deepak',
        'title'  : 'Blog Post2',
        'content' : 'Second post content',
        'date_posted' : 'April 11, 2021'
    }
]

def home_view(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request,'userblog/blog.html', context)


from django.views.generic import (
    ListView,DetailView,CreateView,UpdateView,DeleteView )

class PostListView(ListView):
    model = Post
    template_name = 'userblog/blog.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False


class UserPostListView(ListView):
    model = Post
    template_name = 'userblog/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user)






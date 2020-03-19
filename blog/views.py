from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView
)

# function based view
def home(request):
    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

# class based view
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' 
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    # looking for <app>/<model>_<view_type>.html

class PostCreateView(CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self , form):
        form.instance.author = self.request.user
        return super().form_valid(form)

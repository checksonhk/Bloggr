from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# posts = [
#     {'author': 'James',
#      'title': 'Blog Plot 1',
#      'content': 'First Post Content',
#      'date_posted': 'August 27, 2018'},
#     {'author': 'Anna',
#      'title': 'Blog Plot 2',
#      'content': 'Second Post Content',
#      'date_posted': 'August 28, 2018'},
# ]


def home(request):
    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

# Create your views here.

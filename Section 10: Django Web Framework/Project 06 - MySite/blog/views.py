from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import HttpResponse

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def post(request, slug):
    print(slug)
    posts = Post.objects.all()
    return render(request, 'post.html', {
        'post': get_object_or_404(Post, slug=slug),
        'posts': posts
    })

def about(request):
    return render(request, 'about.html', {})





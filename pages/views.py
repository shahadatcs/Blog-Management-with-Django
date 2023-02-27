from django.shortcuts import render
from blog.models import Post

# Create your views here.
def index(request):
    post = Post.objects.order_by('-created_on').filter(status=1)[:2]
    context = {
        'post': post
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')


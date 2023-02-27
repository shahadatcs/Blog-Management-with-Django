from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from . models import Post

# Create your views here.
def Blog_Entries(request):
   blog_list = Post.objects.order_by('-created_on').filter(status=1)
   paginator = Paginator(blog_list, 4)
   page = request.GET.get('page')
   post = paginator.get_page(page)
   context ={
        'post': post
    }
   return render(request, 'blog/Blog_Entries.html', context)
'''
def Post_Details(request):
    post = Post.objects.order_by('-created_on').filter(status=1)
    context ={
        'post': post
    }
    return render(request, 'blog/Post_Details.html',context)

'''


def Detials(request, post_id):
    post = get_object_or_404(Post, id = post_id )
    context ={
        'post': post
    }
    
    return render(request, 'blog/Detials.html',context)

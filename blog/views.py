from django.shortcuts import render

# Create your views here.
def blog_E(request):
    return render(request, 'blog/blog_e.html')

def blog_P(request):
    return render(request, 'blog/blog_d.html')
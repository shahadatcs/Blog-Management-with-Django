from django.urls import path
from . import views

urlpatterns = [
    path('entire', views.blog_E, name='blogentires'),
    path('post', views.blog_P, name='blogdetails'),
    
]


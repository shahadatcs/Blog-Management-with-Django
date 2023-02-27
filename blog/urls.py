from django.urls import path
from . import views

urlpatterns = [
    path('Blog_Entries', views.Blog_Entries, name='Blog_Entries'),
    #path('Post_Details', views.Post_Details, name='Post_Details'),
    path('<int:post_id>', views.Detials, name='Detials'),
    
]


from django.db import models
from django.contrib.auth.models import User
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
# Create your models here.
class Post(models.Model):
    tag = models.CharField(max_length=200, unique=False)
    title = models.CharField(max_length=200, unique=True)
    category = models.CharField(max_length=200, unique=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    update_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    status = models.IntegerField(choices=STATUS, default=0)
    
    class Meta:
        ordering = ['-created_on']
        
    def __str__(self):
       return self.title
   
    #def get_absolute_url(self):
        #return self.slug


    
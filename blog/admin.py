from django.contrib import admin
from . models import Post
# Register your models here.
class postAdmin(admin.ModelAdmin):
    list_display = ('id','tag','title','status','created_on')
    list_filter = ('status',)
    search_fields = ('title', 'content','tag','category')
    list_display_links = ('id', 'title')
    list_per_page = 25

admin.site.register(Post, postAdmin)

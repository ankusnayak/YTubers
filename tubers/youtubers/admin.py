from django.contrib import admin
from .models import Youtuber
from django.utils.html import format_html

class YtAdmin(admin.ModelAdmin):

    def myphoto(self, object):
        return format_html('<img src="{}" width="40"/>'.format(object.photo.url))
    #list of props that shown in the admin pannel
    list_display = ('id', 'name','myphoto', 'subs_count', 'is_featured')
    # columns or props by which we can search or sort out
    search_fields = ('name', 'camera_type')
    # porps by which we can filter
    list_filter = ('city', 'camera_type')
    # clickable links which goes to the details
    list_display_link = ('id', 'name')
    list_editable = ('is_featured',)
    

    
# Register your models here.
admin.site.register(Youtuber,YtAdmin)
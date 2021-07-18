from django.contrib import admin
from .models import Post, Tag

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'dsuser', 'title', 'content', 'img_src', 'create_date')


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
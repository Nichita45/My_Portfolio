from django.contrib import admin
from .models import Tag, Post

class PostAdmin(admin.ModelAdmin):
    pass
class TagAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
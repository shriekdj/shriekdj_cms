from django.contrib import admin

# Register your models here.
from .models import NewsLetter, Post, PostMeta

admin.site.register(NewsLetter)
admin.site.register(Post)
admin.site.register(PostMeta)

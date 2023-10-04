from django.contrib import admin

# Register your models here.
from blog.models import Profile, Post, Tag

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post

    list_display = (
        "id",
        "title",
        "subtitle",
        "slug",
        "published_at",
        #"is_published",
    )
    list_filter = (
        #"is_published",
        "published_at",
    )
    list_editable = (
        "title",
        "subtitle",
        "slug",
        "published_at",
        #"is_published",
    )
    search_fields = (
        "title",
        "subtitle",
        "slug",
        "content",
    )
    prepopulated_fields = {
        "slug": (
            "title",
            "subtitle",
        )
    }
    date_hierarchy = "published_at"
    save_on_top = True

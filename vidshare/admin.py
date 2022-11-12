from django.contrib import admin
from .models import Video, Author, Category
# Register your models here.

class VideoAdmin(admin.ModelAdmin):
    list_filter = ("date",)
    list_display = ("title", "date",)
    prepopulated_fields = {"slug": ("title",)}

class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("first_name", "last_name")}

admin.site.register(Video, VideoAdmin)

admin.site.register(Author ,AuthorAdmin)

admin.site.register(Category)
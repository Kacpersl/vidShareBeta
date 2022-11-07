from django.contrib import admin
from .models import Video, Author, Category
# Register your models here.

class VideoAdmin(admin.ModelAdmin):
    list_filter = ("date",)
    list_display = ("title", "date",)
    prepopulated_fields = {"slug": ("title",)}



admin.site.register(Video, VideoAdmin)

admin.site.register(Author)

admin.site.register(Category)
from django.contrib import admin
from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'heading', 'created_at')
    list_filter = ('heading',)
    search_fields = ('heading',)

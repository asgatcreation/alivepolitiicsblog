from django.contrib import admin
from .models import *


# Register your models here.

class TagTublerInline(admin.TabularInline):
    model = Tag

class PostAdmin(admin.ModelAdmin):
    inlines=[TagTublerInline]
    list_display = ['title','author','date','status','section','main_post']
    list_editable = ['status','section','main_post']
    search_fields = ['title','section',]

admin.site.register(Category)
admin.site.register(Post,PostAdmin)
admin.site.register(Tag)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    #inlines=[TagTublerInline]
    list_display = ['name', 'body', 'active', 'post', 'email', 'created_on']
    #list_filter = ['active', 'created_on']
    list_editable = ['active']
    search_fields = ['name', 'email', 'body']
    actions = ['approve_comments','disapprove_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
    def disapprove_comments(self, request, queryset):
        queryset.update(active=False)
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content_size','status', 'created_at', 'updated_at']

    actions = ['make_published', 'make_draft']

    def content_size(self, post):
        return mark_safe('{}'.format(len(post.content)))
    content_size.short_description = '글자수'

    def make_published(self,request, queryset):
        updated_count = queryset.update(status='p')
        self.message_user(request, '{}건의 포스팅을 Published상태로 변경'.format(updated_count))
    make_published.short_description = '지정 포스팅을 Published상태로 변경합니다.'

    def make_draft(self,request, queryset):
        updated_count = queryset.update(status='d')
        self.message_user(request, '{}건의 포스팅을 Draft상태로 변경'.format(updated_count))
    make_draft.short_description = '지정 포스팅을 Draft상태로 변경합니다.'

#admin.site.register(Post, PostAdmin)
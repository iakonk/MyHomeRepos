from django.contrib import admin
from coookit.models import Articles, UserComments
from django_summernote.admin import SummernoteModelAdmin


class ArticlesAdmin(SummernoteModelAdmin):
        list_display = ('header', 'negative_feedback', 'positive_feedback', 'content', 'article_type', 'created_date', 'modified_date', 'publish')
        list_filter = ['header']


class UserCommentsAdmin(admin.ModelAdmin):
        pass


admin.site.register(Articles, ArticlesAdmin)
admin.site.register(UserComments, UserCommentsAdmin)

from django.contrib import admin
from coookit.models import Articles


class ArticlesAdmin(admin.ModelAdmin):
        list_display = ('header', 'negative_feedback', 'positive_feedback', 'content', 'article_type', 'created_date', 'modified_date')
        list_filter = ['header']
admin.site.register(Articles, ArticlesAdmin)



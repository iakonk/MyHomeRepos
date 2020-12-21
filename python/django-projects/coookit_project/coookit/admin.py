from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from coookit.models import (Documents,
                            Comments)


class DisabledLogger(object):
    def log_addition(self, *args):
        return

    def log_change(self, *args):
        return

    def log_deletion(self, *args):
        return


class DocumentsAdmin(DisabledLogger, SummernoteModelAdmin):
    list_filter = ['header', 'topic']


class CommentsAdmin(DisabledLogger, admin.ModelAdmin):
    list_display = [
        "text"
    ]


admin.site.register(Documents, DocumentsAdmin)
admin.site.register(Comments, CommentsAdmin)

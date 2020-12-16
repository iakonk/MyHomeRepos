from django.contrib import admin
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

from coookit import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # Main content
    url(r'^$', views.home, name='home'),

    # read the article
    url(r'^document_read/(?P<doc_id>[0-9]+)/$', views.document_read, name='document_read'),

    # work with user comments
    url(r'user_comments/(?P<article_id>[0-9]+)/$', views.user_comments, name='user_comments'),

    # Django summernote editor
    url(r'^summernote/', include('django_summernote.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT + settings.MEDIA_URL)

from django.conf.urls import include, url
from django.contrib import admin
from coookit import views as home_views
from django.conf import settings
from django.conf.urls.static import static
from os import path

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # Main content
    url(r'^$', home_views.home, name='home'),

    # read the article
    url(r'^article/(?P<article_id>[0-9]+)/$', home_views.read_article, name='read_article'),

    # work with user comments
    url(r'user_comments/(?P<article_id>[0-9]+)/$', home_views.user_comments, name='user_comments'),

    # send email
    url(r'^send_email/$', home_views.email2_moderator, name='send_email'),

    # Django summernote editor
    url(r'^summernote/', include('django_summernote.urls')),

] + static(settings.MEDIA_URL, document_root=path.join(settings.MEDIA_ROOT, settings.MEDIA_URL))

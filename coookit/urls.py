from django.conf.urls import include, url
from django.contrib import admin
from coookit import views as home_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # Main content
    url(r'^$', home_views.home, name='home'),

    # read the article
    url(r'^article/(?P<article_id>[0-9]+)/$', home_views.read_article, name='read_article'),

    # send email
    url(r'^send_email/$', home_views.email2_moderator, name='send_email'),

    # https://django-tinymce.readthedocs.org/en/latest/usage.html
    url(r'^tinymce/', include('tinymce.urls')),

    # http://django-allauth.readthedocs.org/en/latest/installation.html
    url(r'^accounts/', include('allauth.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

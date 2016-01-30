from django.conf.urls import include, url
from django.contrib import admin
from home import views as home_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # Main content
    url(r'^$', home_views.home, name='home'),

    # read the article
    url(r'^article/(?P<article_id>[0-9]+)/$', home_views.read_article, name='read_article'),

    # https://django-tinymce.readthedocs.org/en/latest/usage.html
    url(r'^tinymce/', include('tinymce.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

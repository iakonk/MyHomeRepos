from django.db import models
from django.conf import settings
from easy_thumbnails.fields import ThumbnailerImageField


class TimeStampModel(models.Model):
    """
    An abstract base class model that provides self-updating 'created' and 'modified' fields.
    We could manually add these fields to each and every model, but that`s a lot of work and
    ads the risk of human error.
    We set this class to an abstarct in order to avoid creating separate table for it.
    Each class, that inherits this model, will inherit below fields
    """
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ArticlesQuerySet(models.QuerySet):
    """
    Filter articles by default - only published=True
    """
    def published(self):
        return self.filter(publish=True)


class Articles(TimeStampModel):
    """
    Model describes article fields
    Each Article has required field "ARTICLE_TYPE" for filtering purpose
    ARTICLE_VALID_TYPES list contains all possible choices

    Markup handling for Django using the TinyMCE:
        https://django-tinymce.readthedocs.org/en/latest/usage.html

    Each Header image will have additional thumbnail image,
    That will be generated when article is saved to speed up the process
        https://pypi.python.org/pypi/easy-thumbnails
        https://easy-thumbnails.readthedocs.org/en/2.1/usage/#overview
    """

    # Bootstrap Navigation bar on templates/headers.html page base on below values
    # Make sure , href id is the same as below
    ARTICLE_TYPES = (
        ('D', 'Deployment'),
        ('V', 'Development'),
        ('N', 'Networking'),
        ('O', 'Other'),
    )
    header = models.CharField('Header', max_length=100)
    header_image = ThumbnailerImageField('Image header', resize_source=dict(size=(1024, 250), crop="0,15"),
                                         upload_to=settings.MEDIA_URL)
    thumbnail = ThumbnailerImageField('Thumbnail', resize_source=dict(size=(700, 467)), upload_to=settings.MEDIA_URL)
    negative_feedback = models.IntegerField('Negative Feedback count', default=0)
    positive_feedback = models.IntegerField('Positive Feedback count', default=0)
    article_type = models.CharField('Article type', max_length=2, choices=ARTICLE_TYPES, default=ARTICLE_TYPES[0][0])
    content = models.TextField('Article body')
    publish = models.BooleanField('Public visibility', default=False)

    objects = ArticlesQuerySet.as_manager()

    def __unicode__(self):
        return self.header

    class Meta:
        ordering = ["-modified_date"]


class UserComments(TimeStampModel):
    text = models.TextField('User Comments')
    article_id = models.ForeignKey(Articles, default=None)

    def __unicode__(self):
        return self.text

    class Meta:
        ordering = ["-created_date"]
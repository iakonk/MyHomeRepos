from django.db import models
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


class DocumentsQuerySet(models.QuerySet):
    """
    Filter articles by default - only published=True
    """
    def visible(self):
        return self.filter(visible=True)


class Documents(TimeStampModel):
    DEVELOPMENT = 'Development'
    DEPLOYMENT = 'Deployment'
    LINUX = 'Linux'
    NETWORKING = 'Networking'
    OTHER = 'Other'
    TOPIC_CHOICES = (
        (DEVELOPMENT, DEVELOPMENT),
        (DEPLOYMENT, DEPLOYMENT),
        (LINUX, LINUX),
        (NETWORKING, NETWORKING),
        (OTHER, OTHER),
    )
    thumbnail = ThumbnailerImageField('Thumbnail',
                                      resize_source=dict(size=(700, 467)),
                                      upload_to='uploads')
    likes = models.IntegerField('Likes', default=0)
    dislikes = models.IntegerField('Dislikes', default=0)
    header = models.CharField(max_length=100)
    topic = models.CharField(max_length=15, choices=TOPIC_CHOICES, default=OTHER)
    body = models.TextField()
    visible = models.BooleanField('Public visibility', default=False)

    objects = DocumentsQuerySet.as_manager()

    def __unicode__(self):
        return self.header

    def __str__(self):
        return self.header

    class Meta:
        ordering = ["-modified_date"]
        unique_together = ("topic", "header")


class Comments(TimeStampModel):
    text = models.TextField('User Comments')
    doc_id = models.ForeignKey(Documents, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.text

    class Meta:
        ordering = ["-created_date"]

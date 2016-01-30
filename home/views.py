from django.shortcuts import render_to_response
from django.http import Http404
from home.models import Articles


def home(request):
    """
    Gets as few data as possible for a better performance
    :param request:
    :return: List of all found articles
    """
    try:
        articles = Articles.objects.all().values('id', 'header', 'negative_feedback', 'positive_feedback',
                                                 'article_type', 'thumbnail', 'created_date').order_by('created_date',
                                                                                                       'modified_date')
        article_types = Articles.ARTICLE_TYPES
    except ValueError:
        # return page with error messages with local variables
        assert False
        raise Http404()
    return render_to_response("index.html", locals())


def read_article(request, article_id):
    """
    Read article from database
    :param request:
    :param article_id: id of the article
    :return: article fields
    """
    try:
        article = Articles.objects.get(id=article_id)
    except ValueError:
        # return page with error messages with local variables
        assert False
        raise Http404()
    return render_to_response("article.html", locals())

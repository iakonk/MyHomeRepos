from django.shortcuts import render_to_response
from django.http import Http404
from coookit.models import *
from forms import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core import serializers


def home(request):
    """
    Gets as few data as possible for a better performance
    :param request:
    :return: List of all found articles
    """
    try:
        articles = Articles.objects.published().values(
            'id', 'header', 'negative_feedback', 'positive_feedback',
            'article_type', 'thumbnail', 'created_date')
        article_types = Articles.ARTICLE_TYPES
    except ValueError:
        raise Http404()
    return render_to_response("index.html", locals())


def read_article(request, article_id):
    """
    Read article from database by ID
    :param request:
    :param article_id: id of the article
    :return: article fields
    """
    try:
        article = Articles.objects.get(id=article_id)
        form = UserCommentsForm()
    except ValueError:
        # return page with error messages with local variables
        assert False
        raise Http404()
    return render_to_response("article.html", locals())


@csrf_exempt
def user_comments(request, article_id):
    """
    Read or post user comments
    Accept only valid comments
    :param request:
    :param article_id: comments will be always bound to article_id
    :return: json response
    """
    if request.method == 'POST':
        form = UserCommentsForm(request.POST)
        if form.is_valid():
            new_comment = UserComments(text=request.POST['comment'], article_id_id=int(article_id))
            new_comment.save()
            return HttpResponse('<h3>done</h3>')
    if request.method == 'GET':
        data = serializers.serialize("json", UserComments.objects.filter(article_id=article_id))
        return HttpResponse(data, content_type='application/json')
    else:
        return HttpResponse({}, content_type='application/json')


def email2_moderator(request):
    """
    Request is triggered from "Contact Form" on index.html or when reading an article.
    User provides own email/name/message body.
    Moderators email stay always hidden.
    :param request:
    :return: send email to the moderator
    """
    import smtplib
    if request.method == 'POST':
        reply_to = request.POST['reply_to']
        auth_name = request.POST['auth_name']
        message = request.POST['message']

        GMAIL_USER = '@gmail.com'
        GMAIL_PWD = ''
        SUBJECT = 'Email sent from coookit , author: %s' % auth_name

        # Prepare actual message
        message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (reply_to, ", ".join(GMAIL_USER), SUBJECT, message)

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(GMAIL_USER, GMAIL_PWD)
            server.sendmail(reply_to, GMAIL_USER, message)
            server.close()
            print('successfully sent the mail')
        except:
            print("failed to send mail")

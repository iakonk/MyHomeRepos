from django.shortcuts import render_to_response
from django.http import Http404
from coookit.models import Articles


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

        GMAIL_USER = 'konkina.iana@gmail.com'
        GMAIL_PWD = 'G00gle123'
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
            print 'successfully sent the mail'
        except:
            print "failed to send mail"
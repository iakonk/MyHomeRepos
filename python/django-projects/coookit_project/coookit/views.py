from django.core import serializers
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from coookit.models import (Documents,
                            Comments)
from coookit.forms import UserCommentsForm


def _topics_with_documents():
    return Documents.objects.visible().order_by('topic').values_list('topic', flat=True).distinct()


def home(request):
    docs_on_page = 8
    init_page_num = 1

    section = request.GET.get('section')
    page_number = request.GET.get('page', init_page_num)
    topics = _topics_with_documents()

    aggr = {}
    documents = Documents.objects.visible().order_by('topic')
    for one_doc in documents:
        aggr.setdefault(one_doc.topic, [])
        aggr[one_doc.topic].append(one_doc)

    for topic, docs in aggr.items():
        paginator = Paginator(docs, docs_on_page)
        if topic == section:
            page = paginator.get_page(page_number)
        else:
            page = paginator.get_page(init_page_num)
        aggr[topic] = page
    return render(request, "index.html", {'documents': aggr, 'topics': topics})


def document_read(request, doc_id):
    topics = _topics_with_documents()
    document = get_object_or_404(Documents, id=doc_id)
    return render(request, "document.html", {'document': document, 'topics': topics})


@csrf_exempt
def user_comments(request, article_id):
    if request.method == 'POST':
        form = UserCommentsForm(request.POST)
        if form.is_valid():
            new_comment = Comments(text=request.POST['comment'], article_id_id=int(article_id))
            new_comment.save()
            return HttpResponse('<h3>done</h3>')
    if request.method == 'GET':
        data = serializers.serialize("json", Comments.objects.filter(article_id=article_id))
        return HttpResponse(data, content_type='application/json')
    else:
        return HttpResponse({}, content_type='application/json')

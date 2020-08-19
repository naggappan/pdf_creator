from django.shortcuts import render
from django.http import HttpResponse

from .models import Document, DocType, DocValue

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, document_id):
    #import pdb;pdb.set_trace()
    doc_id = Document.objects.get(doc_name=document_id)
    values = DocValue.objects.filter(doc_name=doc_id)
    msg = ""
    for i in values:
        msg = msg +  "<p>" + i.print_text + "</p>"

    return HttpResponse(msg)
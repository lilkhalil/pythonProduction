from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
import htmltext
import json
import validators

# Create your views here.
def index(request):
    url = request.GET.get('url')

    if not validators.url(url):
        return HttpResponseBadRequest('400. Bad Request' + '\n' + 'Invalid parameter ' + url + ' is given!')
        
    result = htmltext.gettext(url)
    return HttpResponse(json.dumps(result, indent=4, ensure_ascii=False), content_type = 'application/json')
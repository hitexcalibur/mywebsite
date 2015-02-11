from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def hello(request):
    return render_to_response('base.html',{},context_instance=RequestContext(request))
    #return HttpResponse("Hello world")
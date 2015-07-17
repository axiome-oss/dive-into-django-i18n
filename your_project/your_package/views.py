from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext

def test(request):
    context = RequestContext(request, {'user': request.user})
    return render_to_response('example.html', context_instance=context)

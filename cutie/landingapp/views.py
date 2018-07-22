from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

''' test
def index(request):
    return HttpResponse("You're at the index.")
'''
def index(request):
	return render(
	        request,
	        'index.html',
	        context={}, #empty for now: this is if we want to incorporate data into our landing page
	    )
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
import os
import datetime

def hello(request):
	os.system("echo %s >> 1.text" % (str(datetime.datetime.now())[:19] +": "+request.META['REMOTE_ADDR']))
	return HttpResponse("hello world!")

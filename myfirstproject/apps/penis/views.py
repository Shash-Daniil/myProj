from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello World")

def list(request):
	return HttpResponse("It is list page")
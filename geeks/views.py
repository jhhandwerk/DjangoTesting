from django.shortcuts import render
from django.http import HttpResponse

# relative import of forms
from .models import GeeksModel 
from .forms import GeeksForm
from .forms import TestForm
from .forms import ImageForm


def create_view(request):
	# dictionary for initial data with
	# field names as keys
	context ={}

	# add the dictionary during initialization
	form = GeeksForm(request.POST or None)
	if form.is_valid():
		form.save()
		
	context['form']= form
	return render(request, "create_view.html", context)

def test_view(request):
	# dictionary for initial data with
	# field names as keys
	context ={}

	# add the dictionary during initialization
	form = TestForm(request.POST or None)
	if form.is_valid():
		form.save()
		
	context['form']= form
	return render(request, "test_view.html", context)

def image_view(request):
	# dictionary for initial data with
	# field names as keys
	context ={}

	# add the dictionary during initialization
	form = ImageForm(request.POST or None)
	if form.is_valid():
		form.save()
		
	context['form']= form
	return render(request, "image_view.html", context)

#the code below printed in the log... and the return kept us on the home page (which is 
# nothing) like in the video)
def button_view(request):
    print("hello log")
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")
    




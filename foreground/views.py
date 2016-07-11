from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from foreground.models import Person


# Create your views here.
def index(request):
	return render(request,'index.html')

@csrf_exempt
def email(request):
	if request.method == "POST":
		username = request.POST['username']
		useremail = request.POST['useremail']
		subject = request.POST['subject']
		message = request.POST['message']
		Person.objects.create(name=username,email=useremail,subject=subject,message=message)
	return render(request,'index.html')

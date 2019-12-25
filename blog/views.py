from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def blog(request):
	return render(request,'blog/index.html',{'message':'hey there!'})
	# return HttpResponse('HI THERE!! TESTING')

def register(request):
	print('in the register func---')
	return render(request,'blog/register.html',{'message':'hey there register here!'})


def services(request):
	print('in the services func')
	return render(request,'blog/services.html',{'message':'hey there register here!'})

import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from django.views.generic import View
from .mixins import JsonResponseMixin
from .models import UserProfile

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

#JSONREPONSE
# def fetch_json_example_view(request):
# 	data = {
# 		'content': 'Some Random Text',
# 		'count': 2000
# 	}
# 	return JsonResponse(data)


#Old way of sending json data
def fetch_json_example_view(request):
	data = {
		'content': 'Some Random Text',
		'count': 2000
	}
	json_data = json.dumps(data)
	return HttpResponse(json_data,content_type='application/json')



#json class based view

# class JsonClassBasedExampleView(View):
# 	def get(self,request,*args,**kwargs):
# 		data = {			
# 			'content': 'Some Random Text',
# 			'count': 3000
# 		}
# 		return JsonResponse(data)



#Using the Custom Mixin in class based view

class JsonClassBasedExampleView(JsonResponseMixin,View):
	def get(self,request,*args,**kwargs):
		data = {			
			'content': 'Some Random Text 2',
			'count': 5000
		}
		return self.render_to_json_response(data)


#serialization: Converting the data into dict or basically into different data structure is serialization.


# class SerializedDetailView(View):
# 	def get(self,request,*args,**kwargs):
# 		obj = UserProfile.objects.get(id=1)
# 		data = {
# 			'user': obj.user.username,
# 			'title': obj.title,
# 			'content': obj.content			
# 		}
# 		json_data = json.dumps(data)
# 		return HttpResponse(json_data,content_type='application/json')


class SerializedDetailView(View):
	def get(self,request,*args,**kwargs):
		qs = UserProfile.objects.get(id=1) 
		data = serialize('json',[qs,],fields=['user','content','title']) # fetching one data
		json_data = data
		return HttpResponse(json_data,content_type='application/json')



class SerializedListView(View):
	def get(self,request,*args,**kwargs):
		qs = UserProfile.objects.all() 
		# data = serialize('json',qs,fields=['user','content'])
		# data = serialize('json',qs) # fetches all the fields
		data = serialize('json',qs,fields=['user','content','title'])		
		json_data = data
		return HttpResponse(json_data,content_type='application/json')


#Using models -UserProfileManeger and UserprofileQueryset

class SerializedListModelsView(View):
	def get(self,request,*args,**kwargs):
		qs = UserProfile.objects.all().serialize()  #Already serialized in the models -UserProfileManager
		json_data = qs
		return HttpResponse(json_data,content_type='application/json')


class SerializedDetailModelsView(View):
	def get(self,request,*args,**kwargs):
		qs = UserProfile.objects.get(id=1).serialize()  #Already serialized in the models -UserProfileManager
		json_data = qs
		return HttpResponse(json_data,content_type='application/json')
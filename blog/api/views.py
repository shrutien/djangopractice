from blog.models import UserProfile
from django.http import HttpResponse
from django.views.generic import View
from blog.mixins import HttpResponseMixin
from blog.forms import UserProfileForm

class UserProfileAPIDetailView(HttpResponseMixin,View):
	'''
	Updating,Deleting and Retrivewing (1)- UserProfile Model.
	'''

	is_json = True

	def get(self,request,id,*args,**kwargs):
		obj = UserProfile.objects.get(id=id)
		json_data = obj.serialize()
		# return HttpResponse(json_data,content_type='application/json')
		return self.render_to_response(json_data)

	def post(self,request,*args,**kwargs):
		pass


	def patch(self,request,*args,**kwargs):
		pass

	def delete(self,request,*args,**kwargs):
		pass


class UserProfileAPIListView(HttpResponseMixin,View):	
	'''
	Creating,Updating,Deleting and Retrivewing (all)- UserProfile Model.
	'''
	is_json = True

	def get(self,request,*args,**kwargs):
		qs = UserProfile.objects.all()
		json_data = qs.serialize()
		return self.render_to_response(json_data)
		

	def post(self,request,*args,**kwargs):
		form = UserProfileForm(request.POST or None)

		if form.is_valid():
			obj = form.save(commit=True)
			json_data = {'message': 'Successfully Saved!'}
			return self.render_to_response(json_data)

		json_data = {'message': 'Unknown error'}
		return self.render_to_response(json_data)

		
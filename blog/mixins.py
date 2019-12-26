from django.http import JsonResponse, HttpResponse


# class JsonResponseMixin(object):
# 	def render_to_json_response(self,context,**reponse_kwargs):
# 		return JsonResponse(self.get_data(context),**reponse_kwargs)

# 	def get_data(self,context):
# 		return context


class JsonResponseMixin(object):
	def render_to_json_response(self,context,*args,**kwargs):
		return JsonResponse(self.get_data(context),*args, **kwargs)

	def get_data(self,context):
		return context

class HttpResponseMixin(object):
	is_json = False
	def render_to_response(self,context,*args,**kwargs):
		content_type = 'text/html'
		if self.is_json == True:
			content_type = 'application/json'
		return HttpResponse(self.get_data(context),content_type)

	def get_data(self,context):
		return context
from django.shortcuts import get_object_or_404
from rest_framework.authentication import SessionAuthentication
from rest_framework import permissions
from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework import pagination
from rest_framework.response import Response 
from .serializers import UserStatusSerializer
from status.models import UserStatusUpload
from status.api.permissions import IsOwnerOrReadOnly

class StatusListSearchAPIView(APIView):
	# permission_classes = []
	# authentication_classes = []
	

	def get(self,request,format=None):
		qs = UserStatusUpload.objects.all()
		serializer = UserStatusSerializer(qs,many=True)
		return Response(serializer.data)


	def post(self,request,format=None):
		qs = UserStatusUpload.objects.all()
		serializer = UserStatusSerializer(qs,many=True)
		return Response(serializer.data)


class ListSearchAPIView(generics.ListAPIView):
	#Example API EndPoint: http://127.0.0.1:8008/api/status/?q=test

	# permission_classes = []
	# authentication_classes = []
	serializer_class = UserStatusSerializer
	# queryset = UserStatusUpload.objects.all()

	#SearchQuery
	def get_queryset(self):
		qs = UserStatusUpload.objects.all()
		value = self.request.GET.get('q')
		if value is not None:
			qs =qs.filter(content__icontains=value)
		return qs

#Serializer Form 

# class UserDetail(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'your_template.html'

#     def get(self, request, pk):
#         serializer = UserSerializer(profile)
#         return Response({'serializer': serializer})

#     def post(self, request, pk):
#         user = get_object_or_404(User, pk=pk)
#         serializer = UserSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response({'serializer': serializer})
#         serializer.save()
#         return redirect('some_url_name')  
	

# Serializer Template Form
# link: https://www.django-rest-framework.org/topics/html-and-forms/#field-styles
# {% load rest_framework %}
# <html><body>

#    <form action="{% url 'user_url' pk=user.pk %}" method="POST">
#         {% csrf_token %}
#         {% render_form serializer template_pack='rest_framework/vertical' %} #Serializerform ex: {{ form.as_p }}
#         <input type="submit" value="Save">
#     </form>

# </body></html>


class StatusCreateAPIView(generics.CreateAPIView):
	# permission_classes = []
	# authentication_classes = []
	serializer_class = UserStatusSerializer
	queryset = UserStatusUpload.objects.all()

	# def perform_create(self,serializer):
	# 	serializer.save(user=self.request.user)



class StatusDetailAPIView(generics.RetrieveAPIView):
	# permission_classes = []
	# authentication_classes = []
	serializer_class = UserStatusSerializer
	# queryset = UserStatusUpload.objects.all()	
	lookup_field = 'id' # or 'slug'

	#2nd way of Retrieving.

	def get_object(self,*args,**kwargs):
		kwargs = self.kwargs
		kw_arg = kwargs.get('id')
		queryset = UserStatusUpload.objects.get(id=kw_arg)
		return queryset


class StatusUpdateAPIView(generics.UpdateAPIView):
	# permission_classes = []
	# authentication_classes = []
	serializer_class = UserStatusSerializer
	queryset = UserStatusUpload.objects.all()	
	lookup_field = 'id' # or 'slug'




class StatusDeleteAPIView(generics.DestroyAPIView):
	# permission_classes = []
	# authentication_classes = []
	serializer_class = UserStatusSerializer
	queryset = UserStatusUpload.objects.all()	
	lookup_field = 'id' # or 'slug'



#USING Mixins (CRUD)


class MixinCreateListSearchAPIView(mixins.CreateModelMixin,generics.ListAPIView):
	#Example API EndPoint: http://127.0.0.1:8008/api/status/mixin_create/?q=test

	'''
	To create and display all the data.
	'''

	# permission_classes = []
	# authentication_classes = []
	serializer_class = UserStatusSerializer

	#SearchQuery
	def get_queryset(self):
		qs = UserStatusUpload.objects.all()
		value = self.request.GET.get('q')
		if value is not None:
			qs =qs.filter(content__icontains=value)
		return qs


	def post(self, request,*args,**kwargs):
		return self.create(request,*args,**kwargs)



class MixinUpdateDeleteAPIView(mixins.UpdateModelMixin,mixins.DestroyModelMixin, generics.RetrieveAPIView):
	'''
	To Update and delete the object.
	'''

	# permission_classes = []
	# authentication_classes = []
	serializer_class = UserStatusSerializer
	queryset = UserStatusUpload.objects.all()
	lookup_field = 'id' #or 'slug'

	def put(self, request,*args,**kwargs):
		return self.update(request,*args,**kwargs)

	def delete(self, request,*args,**kwargs):
		return self.destroy(request,*args,**kwargs)


# WithoutUsingMixin Combined Generics API 

class UserStatusDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
	'''
	To Update and delete the object.
	'''
	# permission_classes = []
	# authentication_classes = []
	serializer_class = UserStatusSerializer
	queryset = UserStatusUpload.objects.all()
	lookup_field = 'id' #or 'slug'


#AllMixinsAPI

class UserStatusAllAPIView(mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.ListAPIView):
	'''
	CRUD - Using all the Mixins.
	'''

	# permission_classes = []
	# authentication_classes = []
	serializer_class = UserStatusSerializer
	lookup_field = 'id' #or 'slug'


	#SearchQuery
	def get_queryset(self):
		#GET /api/status/all_data/?q=2
		request = self.request
		qs = UserStatusUpload.objects.all()
		value = request.GET.get('q')
		if value is not None:
			qs =qs.filter(content__icontains=value)
		return qs


	def get_object(self):
		request = self.request
		passed_id = request.GET.get('id',None)
		queryset = self.get_queryset()
		obj = None
		if passed_id is not None:
			obj = get_object_or_404(queryset,id=passed_id)
			self.check_object_permissions(request,obj)
		return obj

	def get(self,request,*args,**kwargs):
		#GET /api/status/all_data/?id=2
		passed_id = request.GET.get('id',None)
		if passed_id is not None:
			return self.retrieve(request,*args,**kwargs)
		return super().get(request,*args,**kwargs)

	def post(self,request,*args,**kwargs):
		return self.create(request,*args,**kwargs)

	def put(self,request,*args,**kwargs):
		return self.update(request,*args,**kwargs)

	def patch(self,request,*args,**kwargs):		
		return self.update(request,*args,**kwargs)

	def delete(self,request,*args,**kwargs):
		return self.destroy(request,*args,**kwargs)


class CustomAPIPagination(pagination.PageNumberPagination):
	page_size = 4



#Permission Classes

class UserPermissionCreateListAPIView(mixins.CreateModelMixin,generics.ListAPIView):
	#Example API EndPoint: http://127.0.0.1:8008/api/status/mixin_create/?q=test

	'''
	To create and display all the data. Including Permission and Authentication Classes
	'''

	permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly] #checks if it is authenticated(logged in) anonymous user read only(GET)
	# authentication_classes = [SessionAuthentication] #checks the type of authentication (OAUTH,JWT)
	serializer_class = UserStatusSerializer

	pagination_class = CustomAPIPagination #Pagination

	#SearchQuery
	def get_queryset(self):
		qs = UserStatusUpload.objects.all()
		value = self.request.GET.get('q')
		if value is not None:
			qs =qs.filter(content__icontains=value)
		return qs


	def post(self, request,*args,**kwargs):
		return self.create(request,*args,**kwargs)


	def perform_create(self, serializer):		
		serializer.save(user=self.request.user)

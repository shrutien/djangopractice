# from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import generics,viewsets
from rest_framework import mixins
from rest_framework import permissions
from rest_framework_jwt.settings import api_settings
from .serializers import UserRegisterSerializer
from .permissions import AnonPermissionOnly

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class AccountsAuthView(APIView):
	permission_classes = [permissions.AllowAny]

	def get(self,request,format=None):
		# qs = UserStatusUpload.objects.all()
		# serializer = UserStatusSerializer(qs,many=True)
		return Response({'username':'','password':''})

	def post(self,request,*args,**kwargs):
		print(request.user)
		if request.user.is_authenticated:
			return Response({'detail':'You are already authenticated'}, status=400)
		data = request.data
		print(data)
		username = data.get('username')
		password = data.get('password')
		user = authenticate(username=username,password=password)
		payload = jwt_payload_handler(user)
		token = jwt_encode_handler(payload)
		return Response({'token': token})
		# qs = User.objects.filter(Q(username__iexact=username)|Q(email__iexact=username)).distinct()
		# if qs.count == 1:
		# 	user_obj = qs.first()
		# 	if user_obj.check_password(password):
		# 		user = user_obj
		# 		payload = jwt_payload_handler(user)
		# 		token = jwt_encode_handler(payload)
		# 		return Response({'token': token})
		# return Response({'detail': 'Invalid Login Credentials.'})

# 2nd Way of Registering new Users 

class RegisterAPIView(generics.CreateAPIView):	
	queryset = User.objects.all()
	serializer_class = UserRegisterSerializer
	permission_classes = [AnonPermissionOnly]

	def get_serializer_context(self, *args, **kwargs):  #to send request method in serializer class (you can now access the request in the serializer class)
		return {'request': self.request}


#REST VIEWSET Example

class UserViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,                     
                     viewsets.GenericViewSet):
    permission_classes = (AnonPermissionOnly, )
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['email', 'id']

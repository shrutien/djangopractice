import datetime
from django.utils import timezone
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings

User = get_user_model()
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER
expire_delta = api_settings.JWT_REFRESH_EXPIRATION_DELTA


class UserSerializer(serializers.ModelSerializer):  
	class Meta:
		model = User
		fields = [
			'id',
			'username',
			'email'
		]


class UserRegisterSerializer(serializers.ModelSerializer):
	password = serializers.CharField(style={'input_type': 'password'}, write_only = True)
	confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only = True)	
	token = serializers.SerializerMethodField(read_only=True)
	expires = serializers.SerializerMethodField(read_only=True)
	# token_response = serializers.SerializerMethodField(read_only=True)

	class Meta:
		model = User
		fields = [
			'username',
			'email',
			'password',
			'confirm_password',
			'token',
			'expires',
			# 'token_response'
		]
		extra_kwargs = {'password': {'write_only': True}}


	def get_token_response(self,obj):
		user = obj
		payload = jwt_payload_handler(user)
		token = jwt_encode_handler(payload)
		context = self.context # you can now get request in serializer class -> method:  get_serializer_context()
		request = context['request']
		print('User authenticated--',request.user.is_authenticated)
		response = jwt_response_payload_handler(token,user,request=request)
		return response

	def get_expires(self,obj):  #instance of the model		
		return timezone.now() + expire_delta - datetime.timedelta(seconds=2000)

	def get_token(self,obj):  #instance of the model
		user = obj
		payload = jwt_payload_handler(user)
		token = jwt_encode_handler(payload)
		return token

	def validate_email(self,value):
		qs = User.objects.filter(email__iexact=value)
		if qs.exists():
			raise serializers.ValidationError('User with this email already exists.')
		return value

	def validate_username(self,value):
		qs = User.objects.filter(username__iexact=value)
		if qs.exists():
			raise serializers.ValidationError('User with this username already exists.')
		return value

	def validate(self,data):
		password = data.get('password')
		confirm_password = data.get('confirm_password')
		if password != confirm_password:
			raise serializers.ValidationError('Password and Confirm Password does not match.')
		return data

	def create(self,validated_data):
		print('validate data==',validated_data)
		user_obj = User(username=validated_data.get('username'),email=validated_data.get('email'))
		user_obj.set_password(validated_data.get('password'))
		user_obj.save()
		return user_obj



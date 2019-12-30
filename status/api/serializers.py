from rest_framework import serializers
from status.models import UserStatusUpload
from accounts.api.serializers import UserSerializer 

class UserStatusSerializer(serializers.ModelSerializer):
	user = UserSerializer(read_only=True) #Nested Serializer TEST API ENDPOINT: /api/status/user_permission_list/

	class Meta:
		model = UserStatusUpload
		fields = [	
			'user',		
			'content',
			'title',
			'upload_image'
		]

		read_only_fields = ['user']  #GET, Read only


	def validate_content(self,value):
		if len(value) > 10000:
			serializers.ValidationError('Content is way too long.')
		return value


	def validate(self,data):
		content = data.get('content',None)
		if content == '':
			content = None
		image = data.get('upload_image',None)
		if content is None and image is None:
			serializers.ValidationError('Content or Image field is required.')
		return data
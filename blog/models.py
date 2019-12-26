import json
from django.db import models
from django.conf import settings
from django.core.serializers import serialize

# Create your models here.

def upload_update_image(instance,filename):
	return "updates/{user}/{filename}".format(user=instance.user,filename=filename)


class UserProfileQuerySet(models.QuerySet):
	#1st way to serialize (objects.all())
	# def serialize(self):
	# 	qs = self
	# 	return serialize('json', qs, fields=('user','content','title'))

	#2nd way to serialize (objects.all())
	def serialize(self):
		qs = list(self.values('user','content','title','id'))		
		return json.dumps(qs)




class UserProfileManager(models.Manager):
	def get_queryset(self):
		return UserProfileQuerySet(self.model,using=self._db)

class UserProfile(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=200,null=True,blank=True)
	content = models.TextField(null=True,blank=True)
	upload_image = models.ImageField(upload_to=upload_update_image,null=True,blank=True)
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	objects = UserProfileManager() #Serializing all objects(objects.all())

	#Serializing the single object(get method)
	#1st way
	# def serialize(self):
	# 	# return serialize('json',[self,],fields=('user','content','title'))
	# 	json_data = serialize('json',[self,],fields=('user','content','title'))
	# 	dict_data = json.loads(json_data) # converts the json data to python dictonary
	# 	data = json.dumps(dict_data[0]['fields'])
	# 	return data

	#Serializing the single object(get method)
	#2nd way
	def serialize(self):
		try:
			image = self.upload_image.url
		except:
			image = ''
		
		data = {
			'id': self.id,
			'user': self.user.username,
			'content': self.content,
			'title': self.title,
			'image': image
		}		
		json_data = json.dumps(data)
		return json_data

	def __str__(self):
		return self.content


	

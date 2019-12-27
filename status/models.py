from django.db import models
from django.conf import settings

# Create your models here.

def upload_update_image(instance,filename):
	return "status/{user}/{filename}".format(user=instance.user,filename=filename)


class UserStatusQuerySet(models.QuerySet):
	pass


class UserStatusManager(models.Manager):
	def get_queryset(self):
		return UserStatusQuerySet(self.model,using=self._db)

class UserStatusUpload(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=200,null=True,blank=True)
	content = models.TextField(null=True,blank=True)
	upload_image = models.ImageField(upload_to=upload_update_image,null=True,blank=True)
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	objects = UserStatusManager()


	class Meta:
		verbose_name = 'Status Post'
		verbose_name_plural = 'Status Posts'


	def __str__(self):		
		return self.content




from django.contrib import admin
from .models import UserStatusUpload
from .forms import UserStatusForm
# Register your models here.

class UserStatusAdmin(admin.ModelAdmin):
	list_display = ('user','content','title')
	form = UserStatusForm
	# class Meta:
	# 	model = UserStatusUpload


admin.site.register(UserStatusUpload,UserStatusAdmin)
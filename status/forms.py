from django import forms
from .models import UserStatusUpload

class UserStatusForm(forms.ModelForm):
	class Meta:
		model = UserStatusUpload
		fields = [
			'user',
			'content',
			'title',
			'upload_image'
		]


	def clean(self,*args,**kwargs):
		data = self.cleaned_data
		content = data.get('content',None)
		if content == '':
			content = None
		image = data.get('upload_image',None)
		if content is None and image is None:
			raise forms.ValidationError('Content or Image is Required') 
		return super().clean(*args,**kwargs)


	def clean_content(self,*args,**kwargs):
		content = self.cleaned_data.get('content',None)
		if len(content) > 300:
			raise forms.ValidationError('Content is too long.')
		return content

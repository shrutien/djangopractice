from django.utils.six import BytesIO
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from status.api.serializers import UserStatusSerializer
from status.models import UserStatusUpload


'''
Serialize a single object
'''

obj = UserStatusUpload.objects.first()
serializer = UserStatusSerializer(obj)
serializer.data #it will be python dict
json_data = JSONRenderer().render(serializer.data) #At this point we've translated the model instance into Python native datatypes. To finalise the serialization process we render the data into json.
print(json_data) 

#Deserialization (First we parse a stream into Python native datatypes then we restore those native datatypes into a dictionary of validated data.)
stream = BytesIO(json_data)
data = JSONParser().parse(stream)
print(data) #type - dict




'''
Serialize a QuerySet

'''

qs = UserStatusUpload.objects.all()
serializer2 = UserStatusSerializer(qs,many=True)
serializer2.data
json_data2 = JSONRenderer().render(serializer2.data)
print(json_data2)

#Deserialization (First we parse a stream into Python native datatypes then we restore those native datatypes into a dictionary of validated data.)
stream2 = BytesIO(json_data2)
data2 = JSONParser().parse(stream2)
print(data2)


'''
Create obj
'''

data3 = {'user': 1}
serializer3 = UserStatusSerializer(data=data3)
if serializer3.is_valid():
	serializer3.save()


'''
Update Obj
'''

old_obj = UserStatusUpload.objects.first()
data_updated = {'content': 'some new data', 'user': 1}
serialier_old_obj = UserStatusSerializer(old_obj,data=data_updated)
if serialier_old_obj.is_valid():
	serialier_old_obj.save()


#No delete in serializers.


#Without Using ModelSerializer just a normal Serializer example.

class UserStatusSerializer(serializers.Serializer):
    content = serializers.TextField()
    title = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return UserStatusUpload.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.content = validated_data.get('content', instance.content)
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance

new_updated_data = {'content': 'some new data', 'title':'new title', 'user': 1}
# .save() will create a new instance. 
serializer = UserStatusSerializer(data=new_updated_data)

# .save() will update the existing `comment` instance.
serializer = UserStatusSerializer(comment, data=new_updated_data)

from django.conf.urls import url
from django.urls import path, include
from .views import(
                ListSearchAPIView,
                StatusCreateAPIView,
                StatusDetailAPIView,
                StatusUpdateAPIView,
                StatusDeleteAPIView,
                MixinCreateListSearchAPIView,
                MixinUpdateDeleteAPIView,
                UserStatusDetailAPIView,
                UserStatusAllAPIView,
                UserPermissionCreateListAPIView)      


urlpatterns = [      
    url(r'^$', ListSearchAPIView.as_view()),
    url(r'^all_data/$', UserStatusAllAPIView.as_view()),
    url(r'^user_permission_list/$', UserPermissionCreateListAPIView.as_view()),
    url(r'^create/$', StatusCreateAPIView.as_view()),
    url(r'^mixin_create/$', MixinCreateListSearchAPIView.as_view()),
    url(r'^detail/(?P<id>\d+)/$', StatusDetailAPIView.as_view()),
    url(r'^mixin_detail/(?P<id>\d+)/$', MixinUpdateDeleteAPIView.as_view()),
    url(r'^user_detail/(?P<id>\d+)/$', UserStatusDetailAPIView.as_view()),
    url(r'^update/(?P<id>\d+)/$', StatusUpdateAPIView.as_view()),
    url(r'^delete/(?P<id>\d+)/$', StatusDeleteAPIView.as_view()),
]


#APIEndPoints

'''
api/status/ -> List and Search
api/status/create/ ->Create 
api/status/detail/1/ -> Detail(Fetch the details)
api/status/update/2/  -> Update(Update the details)
api/status/update/4/  -> Delete

'''

# StatusDetailAPIView,
# StatusUpdateAPIView,
# StatusDeleteAPIView)     
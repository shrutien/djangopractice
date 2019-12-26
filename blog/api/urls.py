from django.conf.urls import url
from .views import ( UserProfileAPIDetailView,
					UserProfileAPIListView
					)

urlpatterns = [
    url(r'^api_detail/(?P<id>\d+)/$', UserProfileAPIDetailView.as_view(), name='api_detail'),
    url(r'^api_list/$', UserProfileAPIListView.as_view(), name='api_list'),
]
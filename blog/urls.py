from django.conf.urls import url
from django.urls import path, include
from .views import ( blog,				   	 
					register, 
					services,
					fetch_json_example_view,
					JsonClassBasedExampleView,
					SerializedDetailView,
					SerializedListView,
					SerializedListModelsView,
					SerializedDetailModelsView)

urlpatterns = [ 	 
    url(r'^$', blog, name='blog'),
    url(r'^api/', include('blog.api.urls')),
    url(r'^services/$', services, name='services'),
    url(r'^register/$', register, name='register'),
    url(r'^fetch_json_data/$', fetch_json_example_view, name='fetch_json_data'),
    url(r'^json_cbv/$', JsonClassBasedExampleView.as_view(), name='json_cbv'),
    url(r'^serialized_detailview/$', SerializedDetailView.as_view(), name='serialized_detailview'),
    url(r'^serialized_listview/$', SerializedListView.as_view(), name='serialized_listview'),
    url(r'^serialized_modelview/$', SerializedListModelsView.as_view(), name='serialized_modelview'),
    url(r'^serialized_modeldetailview/$', SerializedDetailModelsView.as_view(), name='serialized_modeldetailview'),
]
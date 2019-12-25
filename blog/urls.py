from django.conf.urls import url
from .views import blog, register, services


urlpatterns = [
    url(r'^$', blog, name='blog'),
    url(r'^services/$', services, name='services'),
    url(r'^register/$', register, name='register'),

]
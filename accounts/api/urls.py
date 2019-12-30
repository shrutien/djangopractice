from django.conf.urls import url
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework.routers import DefaultRouter
from .views import(
                AccountsAuthView,
                RegisterAPIView,
                UserViewSet)
                     
router = DefaultRouter()
router.register(r'details', UserViewSet, basename='details')

urlpatterns = [      
    url(r'^$', AccountsAuthView.as_view()),
    url(r'^create/$', RegisterAPIView.as_view()),
    url(r'^jwt/$', obtain_jwt_token),
    url(r'^jwt/refresh/$', refresh_jwt_token),
    path('',include(router.urls))
]
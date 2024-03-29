from django.urls import path, include
from profiles_api import views
from rest_framework.routers import DefaultRouter
# from rest_framework import viewsets

router = DefaultRouter()
router.register(r'hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profiles', views.UserProfileViewset)
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginAPIView.as_view()),
    path(r'', include(router.urls)),
]


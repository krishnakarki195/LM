"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import  include, path
from lms.views import *
from rest_framework import routers

#router = routers.DefaultRouter()
#router.register('', LmsViewSet)



urlpatterns = [
    #path('lms/', include(router.urls)),
    #path('lms/', lms),
    #path('lms/<int:id>/',lms_details)
    path('lms/', LmsAPIView.as_view(), name='lms_add'),
    path('lms/<int:id>/edit/', LmsDetailView.as_view(), name='lms_edit'),
    path('lms/<int:id>/delete/', LmsDetailView.as_view(), name='lms_delete'),
    path('lms/generics/', LmsListView.as_view()),
    path('lms/generics/<int:id>/edit/', LmsListView.as_view()),
    path('lms/generics/<int:id>/delete/', LmsListView.as_view()),

]

from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .import views
from .views import *


router=DefaultRouter()
router.register(r'quotes',QuoteViewset,basename='quotes')

urlpatterns=[
    path('',include(router.urls)),
    path('users/',views.UserApiView.as_view(),name='users'),
    path('users/<int:pk>/',views.UserDetailView.as_view(),name='user-details')
]
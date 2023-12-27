from django.urls import path, include
from . import views 
from rest_framework.routers import DefaultRouter
from .views import QuoteUserViewSet,QuoteViewset

router = DefaultRouter()
router.register('quotes', views.QuoteViewset, basename='quotes')
router.register('quoteusers', views.QuoteUserViewSet, basename='quoteusers')

urlpatterns = [
    path('', include(router.urls))
]
from django.shortcuts import render
from rest_framework import viewsets,mixins
from .serializer import *
# Create your views here.
class QuoteViewset(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class=QuoteSerializer
    queryset=Quote.objects.all()

class QuoteUserViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class=QuoteUserSerializer
    queryset=QuoteUser.objects.all()
    
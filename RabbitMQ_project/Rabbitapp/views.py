from django.shortcuts import render
from django.http import Http404
from rest_framework import viewsets,status
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .producer import publish

# Create your views here.
class QuoteViewset(viewsets.ViewSet):
    def list(self,request):
        products=Quote.objects.all()
        serializer=QuoteSerializer(products,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def create(self,request):
        serializer=QuoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            publish('quote_created',serializer.data)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
    def retrive(self,request,pk=None):
        product=Quote.objects.get(pk=pk)
        serializer=QuoteSerializer(product)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def update(self,request,pk=None):
        product=Quote.objects.all()
        serializer=QuoteSerializer(instance=product,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('quote_created',serializer.data)

        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def destroy(self,request,pk=None):
        product=product.objects.get(pk=pk)
        product.delete()
        publish('quote_created',pk)
        return Response('Quote Deleted')
    
class UserApiView(APIView):
    def get(self,_):
        user=User.objects.all()
        return Response(UserSerializer(user,many=True).data)
    
class UserDetailView(APIView):
        def get_user(self,pk):
            try:
                User.objects.get(pk=pk)
            except User.DoesNotExist:
                raise Http404
            
        def get(self,request,pk,format=None):
            user=self.get_user(pk)
            serializer=UserSerializer(user)
            return Response(serializer.data,status=status.HTTP_200_OK)

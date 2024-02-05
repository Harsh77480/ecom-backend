from django.shortcuts import render
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import permissions, generics, status, views
from datetime import datetime, timedelta
from django.db.models import Q
from django.conf import settings
from rest_framework.parsers import MultiPartParser
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import Permission
from .serializers import * 
from rest_framework import permissions, generics, status, views


# Create your views here.
class GetItemList(generics.ListAPIView) : 
    serializer_class = ItemSerializer
    queryset = Item.objects.all() 
    
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = ItemSerializer(queryset, many=True)
        return Response(serializer.data)
    
    # def get(self, request, *args, **kwargs):
    #     queryset = self.queryset
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer,status=status.HTTP_200_OK)


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
from .models import *

class ArraySerializer(serializers.Serializer):
    list = serializers.ListField()

# Create your views here.
class GetItemList(generics.ListAPIView) : 
    serializer_class = ItemSerializer
    queryset = Item.objects.all() 
    
    def list(self, request ,id):

        queryset = self.get_queryset()
        queryset = queryset.filter(category__id = id)

        filters = Q()
        occasion_filters = self.request.GET.getlist('occasion_filter', None)
        if occasion_filters : 
            filters = filters | Q(occasion_filter__in = OccasionValues.objects.filter(title__in=occasion_filters))

        color_filters = self.request.GET.getlist('color_filter', None)
        if color_filters:
            filters = filters | Q(color_filter__in=ColorValues.objects.filter(title__in=color_filters))
        
        pattern_filter = self.request.GET.getlist('pattern_filter', None)
        if pattern_filter:
            filters = filters | Q(pattern_filter__in=PatternValues.objects.filter(title__in=pattern_filter))
        #------already tested with above fields 

        fabric_filter = self.request.GET.getlist('fabric_filter', None)
        if fabric_filter : 
            filters = filters | Q(fabric_filter__in = FabricValues.objects.filter(title__in=fabric_filter))

        season_filter = self.request.GET.getlist('season_filter', None)
        if season_filter:
            filters = filters | Q(season_filter__in=SeasonValues.objects.filter(title__in=season_filter))

        sleeve_length_filter = self.request.GET.get('sleeve_length_filter', None)
        if sleeve_length_filter:
            filters = filters | Q(sleeve_length_filter__in=SleeveLengthValues.objects.filter(title__in=sleeve_length_filter))

        brand_filter = self.request.GET.get('brand_filter', None)
        if brand_filter:
            filters = filters | Q(brand_filter__in=BrandValues.objects.filter(title__in=brand_filter))

        sort_type = self.request.GET.get('sort_type', None)

        filter_data = {
        "occasion_filter": OccasionValuesSerializer(OccasionValues.objects.all(),context={'request': request},many=True).data,
        "fabric_filter": FabricValuesSerializer(FabricValues.objects.all(),context={'request': request}, many=True).data,
        "pattern_filter": PatternValuesSerializer(PatternValues.objects.all(),context={'request': request}, many=True).data,
        "season_filter": SeasonValuesSerializer(SeasonValues.objects.all(),context={'request': request}, many=True).data,
        "sleeve_length_filter": SleeveLengthValuesSerializer(SleeveLengthValues.objects.all(),context={'request': request}, many=True).data,
        "brand_filter": BrandValuesSerializer(BrandValues.objects.all(),context={'request': request}, many=True).data,
        "color_filter": ColorValuesSerializer(ColorValues.objects.all(),context={'request': request}, many=True).data,}
            
        sort_data = {
            "Newest" : { "is_applied" : sort_type == "Newest" },
            "Price_Asc" : { "is_applied" :  sort_type == "Price_Asc"},
            "Price_Desc" : { "is_applied" : sort_type == "Price_Desc"},
        }

        if sort_type == "Price_Asc" :
            queryset = queryset.filter(filters).order_by("discount_price")
        elif sort_type == "Price_Desc" :
            queryset = queryset.filter(filters).order_by("-discount_price")
        else :
            queryset = queryset.filter(filters).order_by("-created_at")

        serializer = ItemSerializer(queryset,context={'request': request}, many=True)
        return Response({"items_list":serializer.data , "filter_data" : filter_data , "sort_data" : sort_data})
    

class GetCategoryList(generics.ListAPIView) : 
    serializer_class = CategorySerializer
    queryset = Category.objects.all().order_by("-created_at")
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = CategorySerializer(queryset,context={'request': request}, many=True)
        return Response({"categories_list":serializer.data})
    
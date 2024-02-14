from rest_framework import serializers
from .models import *


class ItemSerializer(serializers.ModelSerializer) : 
    image = serializers.SerializerMethodField()
    class Meta : 
        model = Item 
        fields = ('id','title' , 'description' ,'image' ,'original_price' , 'discount_price' , 'discount_percent' ,'likes')


    def get_image(self,instance): 
        if instance.image:
                    return self.context['request'].build_absolute_uri(instance.image.url)
        else:
            return None

class CategorySerializer(serializers.ModelSerializer) : 
    items = serializers.SerializerMethodField()
    class Meta : 
        model = Category 
        fields = ( 'id', 'title1','title2','image','items')
    def get_items(self,instance) : 
        return ItemSerializer(Item.objects.filter(category = instance)[:2],context={'request': self.context['request']},many=True).data 

class OccasionValuesSerializer(serializers.ModelSerializer) : 
    is_applied = serializers.SerializerMethodField()
    class Meta : 
        model = OccasionValues
        fields = ['title','is_applied'] 
    def get_is_applied(self,instance) : 
        request = self.context['request']
        OccasionValues = request.GET.getlist('occasion_filter', "")
        return instance.title in OccasionValues


class FabricValuesSerializer(serializers.ModelSerializer):
    is_applied = serializers.SerializerMethodField()

    class Meta:
        model = FabricValues
        fields = ['title', 'is_applied']

    def get_is_applied(self, instance):
        request = self.context.get('request')
        fabric_filter = request.GET.getlist('fabric_filter', "")
        return instance.title in fabric_filter 

class PatternValuesSerializer(serializers.ModelSerializer):
    is_applied = serializers.SerializerMethodField()

    class Meta:
        model = PatternValues
        fields = ['title', 'is_applied']

    def get_is_applied(self, instance):
        request = self.context.get('request')
        pattern_filter = request.GET.getlist('pattern_filter', "")
        return  instance.title in pattern_filter 

class SeasonValuesSerializer(serializers.ModelSerializer):
    is_applied = serializers.SerializerMethodField()

    class Meta:
        model = SeasonValues
        fields = ['title', 'is_applied']

    def get_is_applied(self, instance):
        request = self.context.get('request')
        season_filter = request.GET.getlist('season_filter', "")
        return instance.title in season_filter

class SleeveLengthValuesSerializer(serializers.ModelSerializer):
    is_applied = serializers.SerializerMethodField()

    class Meta:
        model = SleeveLengthValues
        fields = ['title', 'is_applied']

    def get_is_applied(self, instance):
        request = self.context.get('request')
        sleeve_length_filter = request.GET.getlist('sleeve_length_filter', "")
        return instance.title in sleeve_length_filter

class BrandValuesSerializer(serializers.ModelSerializer):
    is_applied = serializers.SerializerMethodField()

    class Meta:
        model = BrandValues
        fields = ['title', 'is_applied']

    def get_is_applied(self, instance):
        request = self.context.get('request')
        brand_filter = request.GET.getlist('brand_filter', "")
        return instance.title in brand_filter

class ColorValuesSerializer(serializers.ModelSerializer):
    is_applied = serializers.SerializerMethodField()

    class Meta:
        model = ColorValues
        fields = ['title', 'is_applied']

    def get_is_applied(self, instance):
        request = self.context.get('request')
        color_filter = request.GET.getlist('color_filter', "")
        return  instance.title in color_filter
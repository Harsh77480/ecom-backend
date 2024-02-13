from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.



class Category(models.Model):
    title1 = models.CharField(max_length=12)
    title2 = models.CharField(max_length=12)
    created_at = models.DateTimeField(auto_now_add=True)    
    def __str__ (self) :
        return self.title
    def clean(self) :
        super().clean()
        if len(self.title1) > 12 :
            raise ValidationError({'title1': 'length cannot exceed 12'})
        if len(self.title2) > 12 :
            raise ValidationError({'title2': 'length cannot exceed 12'})


class ColorValues(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title 
    def clean(self) :
        super().clean()
        if len(self.title) > 12 :
            raise ValidationError({'title': 'length cannot exceed 12'})


class FabricValues(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title 
    def clean(self) :
        super().clean()
        if len(self.title) > 12 :
            raise ValidationError({'title': 'length cannot exceed 12'})


class PatternValues(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title 
    def clean(self) :
        super().clean()
        if len(self.title) > 12 :
            raise ValidationError({'title': 'length cannot exceed 12'})


class BrandValues(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title 
    def clean(self) :
        super().clean()
        if len(self.title) > 12 :
            raise ValidationError({'title': 'length cannot exceed 12'})


class OccasionValues(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title 
    def clean(self) :
        super().clean()
        if len(self.title) > 12 :
            raise ValidationError({'title': 'length cannot exceed 12'})


class SeasonValues(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title 
    def clean(self) :
        super().clean()
        if len(self.title) > 12 :
            raise ValidationError({'title': 'length cannot exceed 12'})


class SleeveLengthValues(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title 
    def clean(self) :
        super().clean()
        if len(self.title) > 12 :
            raise ValidationError({'title': 'length cannot exceed 12'})

class Item(models.Model) : 
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=250) 
    image = models.FileField(upload_to='item_images/',null=True)
    color_filter = models.ManyToManyField(to=ColorValues,blank=True) 
    brand_filter = models.ManyToManyField(to=BrandValues,blank=True)
    sleeve_length_filter = models.ManyToManyField(to=SleeveLengthValues,blank=True)
    occasion_filter = models.ManyToManyField(to=OccasionValues,blank=True)
    season_filter = models.ManyToManyField(to=SeasonValues,blank=True)
    fabric_filter = models.ManyToManyField(to=FabricValues,blank=True)
    pattern_filter = models.ManyToManyField(to=PatternValues,blank=True)

    # cover = models.FileField 

    original_price = models.PositiveIntegerField(default=0)
    discount_price = models.PositiveIntegerField(default=0)
    discount_percent = models.PositiveIntegerField(default=5)

    likes = models.PositiveBigIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)    
    def clean(self):
        if self.original_price > 99999 :
            self.original_price = 99999
        if self.discount_price > 99999 :
            self.discount_price = 99999 
        if self.discount_percent > 100 :
            self.discount_percent = 100
        

        if self.discount_percent > 0 and self.discount_percent < 99 :
            self.discount_price = self.original_price - ((self.original_price * self.discount_percent)/100)
        else : 
            self.discount_price = self.original_price

    def __str__ (self) :
        return self.title

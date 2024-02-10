from django.db import models

# Create your models here.



class Category(models.Model):
    title1 = models.CharField(max_length=12)
    title2 = models.CharField(max_length=12)
    created_at = models.DateTimeField(auto_now_add=True)    
    def __str__ (self) :
        return self.title
    # cover = models.FileField()

class ColorValues(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title 

class FabricValues(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title 

class PatternValues(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title 

class BrandValues(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title 

class OccasionValues(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title 

class SeasonValues(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title 

class SleeveLengthValues(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title 



class Item(models.Model) : 
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250) 
    image = models.FileField(upload_to='item_images/',null=True,blank=True)
    color_filter = models.ForeignKey(ColorValues,on_delete=models.CASCADE,blank=True,null=True)
    brand_filter = models.ForeignKey(BrandValues,on_delete=models.CASCADE,blank=True,null=True)
    sleeve_length_filter = models.ForeignKey(SleeveLengthValues,on_delete=models.CASCADE,blank=True,null=True)
    occasion_filter = models.ForeignKey(OccasionValues,on_delete=models.CASCADE,blank=True,null=True)
    season_filter = models.ForeignKey(SeasonValues,on_delete=models.CASCADE,blank=True,null=True)
    fabric_filter = models.ForeignKey(FabricValues,on_delete=models.CASCADE,blank=True,null=True)
    pattern_filter = models.ForeignKey(PatternValues,on_delete=models.CASCADE,blank=True,null=True)

    # cover = models.FileField 

    original_price = models.FloatField(default=0)
    discount_price = models.FloatField(default=0)
    discount_percent = models.PositiveIntegerField(default=5)

    likes = models.PositiveBigIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)    
    def clean(self):
        if self.discount_percent > 0 and self.discount_percent < 99 :
            self.discount_price = self.original_price - ((self.original_price * self.discount_percent)/100)
        else : 
            self.discount_price = self.original_price

    def __str__ (self) :
        return self.title

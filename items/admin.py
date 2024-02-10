from django.contrib import admin
from items.models import *
# Register your models here.



admin.site.register(Category) 
admin.site.register(Item) 
admin.site.register(ColorValues) 
admin.site.register(FabricValues) 
admin.site.register(PatternValues) 
admin.site.register(BrandValues) 
admin.site.register(OccasionValues) 
admin.site.register(SeasonValues) 
admin.site.register(SleeveLengthValues) 



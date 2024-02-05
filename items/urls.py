from django.urls import path, include, re_path
from .views import *

urlpatterns = [ 

    path('items/',GetItemList.as_view())

]
from django.urls import path, include, re_path
from .views import *

urlpatterns = [ 
    path('items/<int:id>/',GetItemList.as_view()),
    path('categories/',GetCategoryList.as_view())
]
from app2.views import *
from django.urls import path
app_name="nothing"
urlpatterns=[
    path("rayudu/",rayudu,name='rayudu'),
    path("convey/",convey,name='convey'),
]
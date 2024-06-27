from django.urls import path
from . import views

app_name = 'base'
urlpatterns=[
    path('',  views.home, name="home"),
    path('space/<str:pk>', views.space, name="space"),
    path('create-space/', views.createspace, name="create_space")
]
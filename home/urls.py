from django.urls import path
from .import views

#URL conf module
urlpatterns = [
    path('', views.index),
]

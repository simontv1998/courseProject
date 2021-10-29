from django.urls import path
from clientapp import views

urlpatterns = [
    path('', views.globalStream_action, name='home'),
]
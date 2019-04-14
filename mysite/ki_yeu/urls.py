from django.urls import path
from . import views
urlpatterns = [
    path('', views.ki_yeu, name='ki_yeu'),
]
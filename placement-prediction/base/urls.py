from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('aptitude', views.aptitude, name='aptitude'),
    path('cgpa', views.cgpa, name="cgpa"),
    path('result', views.result, name='result'), 
]
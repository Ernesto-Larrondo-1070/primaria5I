from django.urls import path
from alumno import views

urlpatterns = [
    path('', views.Index_Vista, name='IndexView'),
]
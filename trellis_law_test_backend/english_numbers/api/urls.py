from django.urls import path
from . import views

urlpatterns = [
  path('', views.getData, name='getData'),
  path('num_in_english/', views.get_num_in_english, name='getEnglishNumber'),
]
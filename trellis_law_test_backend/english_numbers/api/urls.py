from django.urls import path
from . import views

urlpatterns = [
  path('num_in_english/', views.num_in_english, name='num-in-english'),
]
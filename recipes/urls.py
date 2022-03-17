from django.urls import path

from . import views

# HTTP REQUEST


urlpatterns = [

    path('', views.home),  # Home
    path('recipes/<id>/', views.recipe),  # Home


]

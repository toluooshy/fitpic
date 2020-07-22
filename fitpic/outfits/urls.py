from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('outfit', views.outfit, name="outfit"),
    path('inventory', views.inventory, name="inventory"),
    path('about', views.about, name="about"),
    path('updateclothing/<str:pk>/', views.updateClothing, name="updateclothing"),
    path('deleteclothing/<str:pk>/', views.deleteClothing, name="deleteclothing")
]
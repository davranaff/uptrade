from django.urls import path

from app import views

urlpatterns = [
    path('menus/', views.home, name='home'),
]

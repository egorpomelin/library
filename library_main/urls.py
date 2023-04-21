from django.urls import path

from library_main import views

urlpatterns = [
    path('', views.index, name='index')
    
]

from django.urls import path, re_path
from library_main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('genre/<int:id>', views.Genre_views, name='genre'),
    path('singl_book/<int:id>', views.Single_book_views, name='single_book')
    
]

from django.urls import path

from .views import create, delete, detail, home, search, update

urlpatterns = [
    path('', home, name='home'),
    path('create/', create, name='create'),
    path('detail/<int:pk>/', detail, name='detail'),
    path('delete/<int:pk>/', delete, name='delete'),    
    path('update/<int:pk>/', update, name='update'),
    path('search/', search, name='search'),
]

from django.urls import path

from .views import create, delete, detail, home, update


urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:pk>/', detail, name='detail'),
    path('create/', create, name='create'),
    path('delete/<int:pk>/', delete, name='delete'),    
    path('update/<int:pk>/', update, name='update'),

]

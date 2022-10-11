
from django.urls import path

from .views import (file_response_example, home, json_response_example,
                    streaming_example)

urlpatterns = [
    path('', home, name='home'),
    path('first/', streaming_example),
    path('second/', json_response_example),
    path('third/', file_response_example),
]

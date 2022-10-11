import time
import os
import requests
from django.http import HttpResponse, StreamingHttpResponse, JsonResponse, FileResponse
from django.conf import settings


def home(request):
    return HttpResponse('Hello World')

def generate_numbers(n):
    for i in range(n):
        yield str(i)
        time.sleep(1)

def streaming_example(request):
    return StreamingHttpResponse(generate_numbers(100))

def json_response_example(request):
    return JsonResponse({'name': 'John', 'age': 30})

def file_response_example(request):
    return FileResponse(open(os.path.join(settings.BASE_DIR, 'Cars.csv'), 'rb'))

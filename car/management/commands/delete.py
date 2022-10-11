from django.core.management.base import BaseCommand

from car.models import Vehicle

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Vehicle.objects.all().delete()
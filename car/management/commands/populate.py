import csv
import os
from django.conf import settings


from datetime import datetime
from car.models import AuctionHouse, Vehicle, Locale, Manufacturer
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def make_lower_and_join(self, value):
        return '_'.join(value.split()).lower()
    
    def get_auction_house(self, value):
        return AuctionHouse.objects.get_or_create(name=value)[0]
    
    def get_locale(self, value):
        return Locale.objects.get_or_create(name=value)[0]
    
    def get_manufacturer(self, value):
        return Manufacturer.objects.get_or_create(name=value)[0]
    
    def get_date(self, value):
        return datetime.strptime(value, '%d/%m/%Y')  

    def get_price(self, value):
        return int(value.replace('$', '').replace(',', ''))

    def handle(self, *args, **kwargs):
        if not Vehicle.objects.all().exists():
            data = []
            file_name = os.path.join(settings.BASE_DIR, "cars.csv")
            with open(file_name, "r", encoding='utf-8') as f:
                reader = list(csv.reader(f, delimiter=","))
                headers = list(map(self.make_lower_and_join, reader[0]))
                rows = reader[1:][::-1]

                m_index = headers.index('manufacturer')
                l_index = headers.index('locale')
                a_index = headers.index('auction_house')

                for row in rows:
                    for _index, col in enumerate(row):
                        if _index == m_index:
                            row[_index] = self.get_manufacturer(col)
                        elif _index == l_index:
                            row[_index] = self.get_locale(col)
                        elif _index == a_index:
                            row[_index] = self.get_auction_house(col)
                        elif 'date' in headers[_index]:
                            row[_index] = self.get_date(col)
                        elif 'price' in headers[_index]:
                            row[_index] = self.get_price(col)
                        else:
                            continue

                    data.append(Vehicle(**dict(zip(headers, row))))

            Vehicle.objects.bulk_create(data)

            self.stdout.write(self.style.SUCCESS("Successfully populated database"))

        else:
            self.stdout.write(self.style.ERROR("Database is not empty"))
import csv
from decimal import Decimal
from django.core.management.base import BaseCommand
from src.models import Location, Category

class Command(BaseCommand):
    help = 'Import data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file to import.')

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file']

        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                try:
                    category, created = Category.objects.get_or_create(name=row['Category'])
                    if row['Longitude']:
                        longitude = Decimal(row['Longitude'])

                    if row['Latitude']:
                        latitude =  Decimal(row['Latitude'])
                        
                    Location.objects.create(
                        mapotic_id=row['MapoticID'],
                        longitude=longitude,
                        latitude=latitude,
                        name=row['Name'],
                        category=category,
                        rating=row['Rating'],
                        image_url=row['Image URL'],
                        import_id=row['Import ID'],
                        description=row['Description'],
                        address=row['Address'],
                        web=row['Web'],
                        email=row['E-mail'],
                        phone_number=row['Phone number'],
                        refreshment=row['Refreshment'],
                        diving=row['Diving'],
                        entrance=row['Entrance'],
                        accessibility_parking=row['Accessibility/parking'],
                        link=row['Link'],
                        video=row['Video'],
                        nudist_beach=row['Nudist beach'],
                        dog_swimming=row['Dog swimming']
                    )
                except Exception as e:
                    print(f"Error processing row {reader.line_num}: {e}")
                    print(row)

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
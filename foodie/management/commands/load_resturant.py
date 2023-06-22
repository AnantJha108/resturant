from csv import DictReader


from django.core.management import BaseCommand
# Import the model 
from foodie.models import Foodie


ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the child data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    help = "Loads data from resurants_small.csv"

    def handle(self, *args, **options):
    
        if Foodie.objects.exists():
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return
            
        for row in DictReader(open('./restaurants_small.csv')):
            child=Foodie(name=row['name'], location=row['location'], items=row['items'],lat_long=row['lat_long'],full_details=row['full_details'])  
            child.save()
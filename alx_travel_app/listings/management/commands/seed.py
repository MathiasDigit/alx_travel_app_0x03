from django.core.management.base import BaseCommand
from listings.models import Listing
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        sample_data = [ 
            {
                "title": "Cosy Apartment in Downtown",
                "description": "A beautiful and cozy apartment in the heart of the city.",
                "address": "234 Tokyo, CityHunter",
                "price_night": 90.88
            },

            {
                "title": "Cosy Apartmen in smalldown",
                "description": "A beautiful and cozy apartment on the outskirts of the city",
                "address": "246 Douala, pk14",
                "price_night": 60.00
            },
        
        ]
        
        for data in sample_data:
            listing, created = Listing.objects.get_or_create(
                title=data['title'],
                defaults={
                    "description": data['description'],
                    "address": data['address'],
                    "price_night": data['price_night']
                }
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f"Created listing: {listing.title}"))
            else:
                self.stdout.write(self.style.SUCCESS(f"Listing already exists: {listing.title}"))


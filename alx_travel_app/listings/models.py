from django.db import models
import uuid
from django.contrib.auth import get_user_model

# Create your models here.

user = get_user_model()

class Listing(models.Model):
    property = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    price_night = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled'),
    ]

    booking_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    property = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='bookings')
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Booking {self.booking_id}"
    

class Review(models.Model):
    review_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    property = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"review {self.review_id}"
    



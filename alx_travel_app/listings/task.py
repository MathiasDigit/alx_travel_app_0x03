from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_booking_confirmation_email(to_email, listing_title):
    subject = 'Reservation confirmation'
    message = 'Your reservation for {listing_title} has been confirmed. Thank you!'
    send_mail(subject, message, 'mathsbel6@gmail.com', [to_email])
     
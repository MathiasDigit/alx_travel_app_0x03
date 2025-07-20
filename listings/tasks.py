from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_booking_confirmation_email(to_email, listing_title):
    print(f"📨 Début de l'envoi d'email à : {to_email} pour la réservation : {listing_title}")

    try:
        subject = 'Reservation confirmation'
        message = f'Your reservation for {listing_title} has been confirmed. Thank you!'

        send_mail(
            subject,
            message,
            'mathsbel6@gmail.com',  # Adresse d’envoi (peut être modifiée dans settings.py aussi)
            [to_email],
            fail_silently=False  # Très important pour afficher les erreurs en cas d’échec
        )

        print("✅ Email envoyé avec succès.")

    except Exception as e:
        print(f"❌ Erreur lors de l'envoi de l'email : {e}")
        raise  # Pour que Celery affiche l’erreur dans les logs

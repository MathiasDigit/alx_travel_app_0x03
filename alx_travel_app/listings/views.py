import requests as http_requests
import uuid
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Listing, Booking, Payment
from .serializers import ListingsSerializer, BookingSerializer
from django.conf import settings
from django.http import HttpResponse
from django.views import View

# Create your views here.
class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingsSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class ChapaPaymentInitView(APIView):
    def post(self, request, booking_id):
        try:
            booking = Booking.objects.get(booking_id=booking_id)
        except Booking.DoesNotExist:
            return Response({"error": "Booking not found"}, status=404)
        
        # Create a unique reference for the transaction
        tx_ref = f"TRX-{booking_id}-{uuid.uuid4().hex[:8]}"
        amount = booking.total_price
        
        # Payload expected by the Chapa API
        data = {
            "amount": str(amount),
            "currency": "ETB",
            "email": booking.user.email,
            "first_name": booking.user.first_name,
            "last_name": booking.user.last_name,
            "tx_ref": tx_ref,
            "callback_url": "http://localhost:8000/api/chapa/callback/",
            "return_url": "http://localhost:8000/payment-success/",
            "customization": {
                "title": "Booking Payment",
                "description": "payment for travel booking"
            }
        }

        headers = {
            "Authorization": f"Bearer {settings.CHAPA_SECRET_KEY}",
            "content-Type": "application/json"
        }

        # Sending the POST request to Chapa
        response = http_requests.post("https://api.chapa.co/v1/transaction/initialize", json=data, headers=headers)
        
        try:
            response_data = response.json()
        except ValueError:
             return Response({
                    "error": "Chapa response not JSON",
                    "status_code": response.status_code,
                    "content": response.text
                }, status=500)

        # Verifying the response
        if response.status_code == 200:
            res_data = response.json()['data']
            # Create the Payment object
            payment = Payment.objects.create(
                booking=booking,
                amount=amount,
                chapa_tx_ref=tx_ref,
                chapa_checkout_url=res_data['checkout_url']
            )
            return Response({
                "payment_url": res_data['checkout_url'],
                "tx_ref": tx_ref   
                }, status=201)
        else:
            print(response.status_code)
            print(response.text)
            return Response({"error": "Failed to initiate payment"}, status=500)

class ChapaVerifyPaymentView(APIView):
    def get(self, requests, tx_ref):
        url = f"https://api.chapa.co/v1/transaction/verify/{tx_ref}"
        headers = {"Authorization": f"Bearer {settings.CHAPA_SECRET_KEY}"}

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json().get("data")
            if data["status"] == "success":
                try:
                    Payment = Payment.objects.get(chapa_tx_ref=tx_ref)
                    Payment.status = "Completed"
                    Payment.save()
                    return Response({"message": "Payment successful"})
                except Payment.DoesNotExist:
                    return Response({"error": "Transaction not found"}, status=404)
            else:
                return Response({"message": "Payment not completed"}, status=400)
        return Response({"error": "Verification failed"}, status=500)


class PaymentSuccessView(View):
    def get(self, request):
        return HttpResponse("Paiement réussi ! Merci pour votre réservation.")

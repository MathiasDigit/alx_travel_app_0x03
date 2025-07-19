from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ListingViewSet, BookingViewSet, ChapaPaymentInitView, ChapaVerifyPaymentView, paymentSuccessView

router = DefaultRouter()
router.register(r'listings', ListingViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('chapa/init/<uuid:booking_id>/', ChapaPaymentInitView.as_view(), name='init-payment'),
    path('chapa/verify/<str:tx_ref>/', ChapaVerifyPaymentView.as_view(), name='verify-payment'),
    path('payment-success/', paymentSuccessView.as_view(), name='payment-success'),
]
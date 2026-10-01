from rest_framework import viewsets
from django.core.mail import send_mail
from .models import Order
from .serializers import OrderSerializer
#from .sms import send_order_sms 
# from mpesa.utils import initiate_stk_push

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('-created_at')
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        # Save the order
        order = serializer.save()

        # Check if the order is marked as paid
        if getattr(order, 'payment_status', False):  # Adjust field name if different
            send_mail(
                subject=f"Order Confirmation #{order.id}",
                message=(
                    f"Hi {order.buyer_name},\n\n"
                    f"Your order #{order.id} has been successfully placed and paid.\n"
                    f"We'll begin processing it shortly. Thank you!"
                ),
                from_email='abuu.yus@gmail.com',  # Replace with your configured sender
                recipient_list=[order.email],
                fail_silently=False,
            )
            # Optionally send SMS
            # send_order_sms(order.phone_number, order.id, order.buyer_name)

        return order

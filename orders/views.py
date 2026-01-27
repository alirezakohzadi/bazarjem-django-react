from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import OrderSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from django.core.mail import send_mail
from django.conf import settings
import threading

def send_order_confirmation_email(user_email, order_details):
    subject = 'تأیید سفارش شما'
    message = f'سفارش شما با موفقیت ثبت شد. جزئیات سفارش:\n{order_details}'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user_email]
    send_mail(subject, message, from_email, recipient_list)

def send_order_confirmation_email_async(user_email, order_details):
    thread = threading.Thread(target=send_order_confirmation_email, args=(user_email, order_details))
    thread.start()


class OrderCreateView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        items = []
        index = 0
        while True:
            prefix = f"items[{index}]"
            if f"{prefix}[product_option]" not in request.data:
                break

            items.append({
                "product_option": request.data.get(f"{prefix}[product_option]"),
                "price": request.data.get(f"{prefix}[price]"),
                "quantity": request.data.get(f"{prefix}[quantity]"),
                "email": request.data.get(f"{prefix}[email]"),
                "phone_number": request.data.get(f"{prefix}[phone_number]"),
                "game_id": request.data.get(f"{prefix}[game_id]"),
                "screenshot": request.FILES.get(f"{prefix}[screenshot]"),
                "address": request.data.get(f"{prefix}[address]"),
            })
            index += 1

        new_data = {
            "total_price": request.data.get("total_price"),
            "items": items,
        }

        serializer = OrderSerializer(data=new_data, context={'request': request})
        if serializer.is_valid():
            order = serializer.save()
            order_details = f"شماره سفارش: {order.id}\n" \
                            f"مبلغ کل: {order.total_price}\n" \
                            f"تعداد محصولات: {len(order.items.all())}"
            user_email = request.user.email
            send_order_confirmation_email_async(user_email, order_details)
            return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

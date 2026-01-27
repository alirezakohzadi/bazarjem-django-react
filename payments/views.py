from django.db import transaction
from django.core.cache import cache
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from decimal import Decimal
from .models import Transaction
from user.models import CustomUser

class TransactionAPIView(APIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        amount = Decimal(request.data.get('amount'))
        transaction_type = request.data.get('transaction_type')

        if not user:
            return Response({"error": "User not found"}, status=status.HTTP_400_BAD_REQUEST)

        if not amount or not transaction_type:
            return Response({"error": "Missing amount or transaction type"}, status=status.HTTP_400_BAD_REQUEST)

        if transaction_type not in ['deposit', 'withdraw']:
            return Response({"error": "Invalid transaction type"}, status=status.HTTP_400_BAD_REQUEST)

        request_key = f"transaction_lock_{user.id}_{amount}_{transaction_type}"
        if cache.get(request_key):
            return Response({"error": "Transaction already in progress. Please try again."}, status=status.HTTP_400_BAD_REQUEST)

        cache.set(request_key, True, timeout=10)

        try:
            with transaction.atomic():
                user = CustomUser.objects.select_for_update().get(id=user.id)

                if transaction_type == 'deposit':
                    user.wallet_balance += amount
                elif transaction_type == 'withdraw':
                    if user.wallet_balance < amount:
                        return Response({"error": "Insufficient funds"}, status=status.HTTP_400_BAD_REQUEST)
                    user.wallet_balance -= amount

                user.save()

                Transaction.objects.create(
                    user=user,
                    amount=amount,
                    transaction_type=transaction_type
                )

                return Response({
                    "status": "Transaction successful",
                    "new_balance": str(user.wallet_balance)
                }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        finally:
            cache.delete(request_key)

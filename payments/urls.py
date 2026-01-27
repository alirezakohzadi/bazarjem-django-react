from django.urls import path
from .views import TransactionAPIView

urlpatterns = [
    path('api/transactions/', TransactionAPIView.as_view(), name='transaction-create'),
]

from django.db import models, transaction
from user.models import CustomUser


class Transaction(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="transactions")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    TRANSACTION_TYPE = (
        ("deposit", "Deposit"),
        ("withdraw", "Withdraw"),
    )
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE)

    def __str__(self):
        return f"{self.user.email} - {self.amount} ({self.transaction_type})"

    def save(self, *args, **kwargs):
        with transaction.atomic():
            # مقدار موجودی را از دیتابیس دریافت کن
            user = CustomUser.objects.select_for_update().get(id=self.user.id)

            if self.transaction_type == 'deposit':
                user.wallet_balance += self.amount
            elif self.transaction_type == 'withdraw':
                if user.wallet_balance < self.amount:
                    raise ValueError("Insufficient funds for withdrawal.")
                user.wallet_balance -= self.amount

            # ذخیره تغییرات در دیتابیس
            user.save(update_fields=['wallet_balance'])

            # مقدار نهایی را در شیء user به‌روز کن
            self.user.wallet_balance = user.wallet_balance

            super().save(*args, **kwargs)  # ذخیره تراکنش

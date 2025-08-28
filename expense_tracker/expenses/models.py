from django.db import models

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('food', 'Food'),
        ('travel', 'Travel'),
        ('shopping', 'Shopping'),
        ('entertainment', 'Entertainment'),
        ('other', 'Other'),
    ]

    PAYMENT_CHOICES = [
        ('cash', 'CASH'),
        ('card', 'CARD'),
        ('upi', 'UPI'),
    ]

    TYPE_CHOICES = [
        ('expense', 'EXPENSE'),
        ('income', 'INCOME'),
    ]

    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    payment_method = models.CharField(max_length=50, choices=PAYMENT_CHOICES, default='upi')
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='expense')
    date = models.DateField()
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.description} - {self.amount}"

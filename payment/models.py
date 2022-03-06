from django.db import models
from core.models.base import BaseEntity

ACCOUNT_CHOICES = (
    ('M', 'Master Card'),
    ('V', 'Visa Card'),
    ('S', 'Stripe'),
    ('B', 'Bank'),
)

PAYMENT_STATUS = (
    ('S', 'Successful'),
    ('p', 'Pending'),
    ('F', 'Failed'),
)


class Payment(BaseEntity):
    amount = models.IntegerField(default=0)
    sender_id = models.CharField(max_length=50, help_text='Which purpose do you want to payment add the sender ID')
    card_number = models.IntegerField(unique=True)
    payment_account = models.CharField(max_length=2, choices=ACCOUNT_CHOICES)
    card_holder_name = models.CharField(max_length=30, blank=True, null=True)
    cvv = models.CharField(max_length=6, unique=True)
    expiry_date = models.DateField()
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS)

    def __str__(self):
        return self.card_number

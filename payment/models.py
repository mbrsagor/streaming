from django.db import models

from films.models import Film
from accounts.models import Timestamp, User


class Purchase(Timestamp):
    quantity = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='film')
    vat = models.DecimalField(default=15.00, max_digits=100, decimal_places=2)

    PAYMENT_TYPES = (
        ('T1', 'CREDIT CARD'),
        ('T2', 'VISA CARD'),
        ('T3', 'BANK'),
        ('T4', 'STRIPE'),
    )
    payment = models.CharField(max_length=2, choices=PAYMENT_TYPES)
    is_download = models.BooleanField(default=False)

    def __str__(self):
        return self.customer.name

    @property
    def get_discount_price(self):
        return self.item.discount_price

    @property
    def total_price(self):
        return self.item.price * self.quantity - self.vat

    @property
    def get_item_name(self):
        return self.item.name

    @property
    def get_customer_name(self):
        return self.customer.name

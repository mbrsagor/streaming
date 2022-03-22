from rest_framework import serializers

from films.models import Purchase


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        read_only_fields = ('customer',)
        fields = [
            'id', 'customer', 'item', 'quantity', 'vat', 'status',
            'payment', 'is_download', 'created_at', 'updated_at'
        ]

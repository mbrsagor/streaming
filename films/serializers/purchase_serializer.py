from rest_framework import serializers

from films.models import Purchase


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        read_only_fields = ('customer',)
        fields = [
            'id', 'customer', 'get_customer_name', 'item', 'get_item_name', 'quantity', 'vat',
            'total_price', 'get_discount_price', 'status', 'payment', 'is_download', 'created_at',
            'updated_at'
        ]

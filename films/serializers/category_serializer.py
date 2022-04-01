from rest_framework import serializers

from films.models import Category


class CategorySerializer(serializers.ModelSerializer):
    parent = serializers.SerializerMethodField()

    class Meta:
        model = Category
        read_only_fields = ('creator',)
        fields = (
            'id', 'name', 'parent', 'creator', 'creator_name',
            'is_active', 'image', 'created_at', 'updated_at'
        )

    def get_parent(self, obj):
        return str(obj.parent)

    # validate name
    def validate_name(self, value):
        if len(value) <= 2:
            raise serializers.ValidationError("Name field is more than al lest one char")
        return value

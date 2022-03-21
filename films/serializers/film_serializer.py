from rest_framework import serializers

from films.models import Film


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        read_only_fields = ('director',)
        fields = [
            'id', 'director', 'name', 'category_name', 'actors', 'producers', 'types',
            'is_publish', 'release_date', 'description', 'price', 'discount_price',
            'image', 'video', 'is_watchable', 'created_at', 'updated_at'
        ]

from rest_framework import serializers

from films.models import Trailer


class TrailerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trailer
        fields = '__all__'

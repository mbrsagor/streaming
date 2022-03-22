from rest_framework import serializers

from films.models import Film, Actor
from films.serializers.trailer_serializer import ActorSerializer


class FilmSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)

    class Meta:
        model = Film
        read_only_fields = ('director',)
        fields = [
            'id', 'director', 'name', 'category_name', 'actors', 'producers', 'types',
            'is_publish', 'release_date', 'description', 'price', 'discount_price',
            'image', 'video', 'is_watchable', 'slug', 'created_at', 'updated_at'
        ]

    def get_or_create_actor(self, actors):
        actor_ids = []
        for actor in actors:
            actor_instance, create = Actor.objects.get_or_create(pk=actor.get('id'), defaults=actor)
            actor_ids.append(actor_instance.pk)
        return actor_ids

    def create_or_update_actor(self, actors):
        actor_ids = []
        for actor in actors:
            actor_instance, create = Actor.objects.update_or_create(pk=actor.get('id'), defaults=actor)
            actor_ids.append(actor_instance.pk)
        return actor_ids

    def create(self, validated_data):
        actors = validated_data.pop('actors', [])
        film = Film.objects.create(**validated_data)
        film.actors.set(self.get_or_create_actor(actors))
        return film

    def update(self, instance, validated_data):
        actors = validated_data.pop('actors', [])
        instance.actors.set(self.create_or_update_actor(actors))
        return instance

    def validate_name(self, value):
        if len(value) <= 3:
            raise serializers.ValidationError("Item name should be more than 2 characters")
        return value

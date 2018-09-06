from .models import IGDBGame, Genre
from rest_framework import serializers


class IGDBGenreSerializer(serializers.ModelSerializer):

	class Meta:

		model = Genre
		fields = '__all__'


class IGDBGameSerializerList(serializers.ModelSerializer):

	genres = IGDBGenreSerializer(many=True)

	class Meta:

		model = IGDBGame
		fields = '__all__'


class IGDBGameSerializerCreate(serializers.ModelSerializer):

	genres = IGDBGenreSerializer(many=True)

	class Meta:
		model = IGDBGame
		fields = '__all__'

	def create(self, validated_data):
		genres = validated_data.pop('genres')
		instance = IGDBGame.objects.create(**validated_data)
		for genre in genres:
			instance.genres.add(genre)
		return instance
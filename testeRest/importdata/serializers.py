from .models import IGDBGame, Genre
from rest_framework import serializers


class IGDBGenreSerializer(serializers.ModelSerializer):

	class Meta:

		model = Genre
		fields = ['name']


class IGDBGameSerializer(serializers.ModelSerializer):

	genres = IGDBGenreSerializer(many=True)

	class Meta:

		model = IGDBGame
		fields = '__all__'